# Audio processing utilities
import ffmpeg

def combine_audio_files(file1, file2, output_file):
    """
    Combine two audio files into one.
    """
    input1 = ffmpeg.input(file1)
    input2 = ffmpeg.input(file2)
    (
        ffmpeg
        .concat(input1, input2, v=0, a=1)
        .output(output_file)
        .run()
    )

def add_background_music(audio_file, music_file, output_file, volume=0.3):
    """
    Add background music to audio file.
    """
    audio = ffmpeg.input(audio_file)
    music = ffmpeg.input(music_file).filter('volume', volume)
    (
        ffmpeg
        .filter([audio, music], 'amix', inputs=2)
        .output(output_file)
        .run()
    )