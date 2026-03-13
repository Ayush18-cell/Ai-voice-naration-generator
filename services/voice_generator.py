import os
from gtts import gTTS
from elevenlabs.client import ElevenLabs
from elevenlabs.core import ApiError
from config import Config
import uuid
import re
from .audio_generator import combine_audio_files

def generate_voice(text, voice_type='gtts', voice_id=None):
    if len(text) > Config.MAX_TEXT_LENGTH:
        raise ValueError(f"Text is too long. Maximum allowed: {Config.MAX_TEXT_LENGTH} characters.")

    filename = f"{uuid.uuid4()}.mp3"
    filepath = os.path.join('static', 'audio', filename)

    if voice_type == 'gtts':
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(filepath)
    elif voice_type == 'elevenlabs':
        if not voice_id:
            raise ValueError("Voice ID is required for ElevenLabs TTS.")
        client = ElevenLabs(api_key=Config.ELEVENLABS_API_KEY)

        # Split text into chunks if too long (ElevenLabs has limits)
        chunks = split_text_into_chunks(text, max_length=2000)  # Adjust based on API limits

        if len(chunks) == 1:
            # Single chunk
            try:
                audio = b"".join(
                    client.generate(
                        text=text,
                        voice=voice_id,
                        model="eleven_multilingual_v2",
                    )
                )
                with open(filepath, 'wb') as f:
                    f.write(audio)
            except ApiError as e:
                raise RuntimeError(
                    f"ElevenLabs TTS failed (status {e.status_code}): {e.body}. "
                    "Update your ElevenLabs plan or use a supported free-tier model."
                )
        else:
            # Multiple chunks: generate each and combine
            temp_files = []
            for i, chunk in enumerate(chunks):
                temp_filename = f"{uuid.uuid4()}_chunk_{i}.mp3"
                temp_filepath = os.path.join('static', 'audio', temp_filename)
                try:
                    audio = b"".join(
                        client.generate(
                            text=chunk,
                            voice=voice_id,
                            model="eleven_multilingual_v2",
                        )
                    )
                    with open(temp_filepath, 'wb') as f:
                        f.write(audio)
                    temp_files.append(temp_filepath)
                except ApiError as e:
                    # Clean up temp files
                    for tf in temp_files:
                        if os.path.exists(tf):
                            os.remove(tf)
                    raise RuntimeError(
                        f"ElevenLabs TTS failed (status {e.status_code}): {e.body}. "
                        "Update your ElevenLabs plan or use a supported free-tier model."
                    )

            # Combine all chunks
            if len(temp_files) > 1:
                combine_audio_files(temp_files[0], temp_files[1], filepath)
                for i in range(2, len(temp_files)):
                    temp_combined = f"{uuid.uuid4()}_combined.mp3"
                    temp_combined_path = os.path.join('static', 'audio', temp_combined)
                    combine_audio_files(filepath, temp_files[i], temp_combined_path)
                    os.rename(temp_combined_path, filepath)

            # Clean up temp files
            for tf in temp_files:
                if os.path.exists(tf):
                    os.remove(tf)
    else:
        raise ValueError("Invalid voice type")

    return filepath

def split_text_into_chunks(text, max_length=2000):
    """
    Split text into chunks, trying to break at sentence boundaries.
    """
    if len(text) <= max_length:
        return [text]

    chunks = []
    sentences = re.split(r'(?<=[.!?])\s+', text)
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 <= max_length:
            current_chunk += sentence + " "
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
            if len(current_chunk) > max_length:
                # If a single sentence is too long, split it
                words = sentence.split()
                temp_chunk = ""
                for word in words:
                    if len(temp_chunk) + len(word) + 1 <= max_length:
                        temp_chunk += word + " "
                    else:
                        if temp_chunk:
                            chunks.append(temp_chunk.strip())
                        temp_chunk = word + " "
                if temp_chunk:
                    current_chunk = temp_chunk
                else:
                    current_chunk = sentence + " "

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks