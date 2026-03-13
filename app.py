from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import os
from werkzeug.utils import secure_filename
from config import Config
from services.voice_generator import generate_voice
from utils.file_handler import allowed_file, save_uploaded_file, extract_text

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY
app.config['MAX_CONTENT_LENGTH'] = Config.MAX_CONTENT_LENGTH

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form.get('text')
    voice_type = request.form.get('voice_type', 'gtts')
    voice_id = request.form.get('voice_id') if voice_type == 'elevenlabs' else None

    if not text:
        flash('Please enter some text to narrate.')
        return redirect(url_for('index'))

    try:
        audio_path = generate_voice(text, voice_type, voice_id)
        return send_file(audio_path, as_attachment=True)
    except Exception as e:
        flash(f'Error generating voice: {str(e)}')
        return redirect(url_for('index'))

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('index'))

    if file and allowed_file(file.filename, Config.ALLOWED_EXTENSIONS):
        filename = secure_filename(file.filename)
        file_path = save_uploaded_file(file, filename)
        extension = filename.rsplit('.', 1)[1].lower()
        try:
            text = extract_text(file_path, extension)
        except Exception as e:
            os.remove(file_path)
            flash(f'Error reading file: {str(e)}')
            return redirect(url_for('index'))
        os.remove(file_path)  # Clean up

        voice_type = request.form.get('voice_type', 'gtts')
        voice_id = request.form.get('voice_id') if voice_type == 'elevenlabs' else None

        try:
            audio_path = generate_voice(text, voice_type, voice_id)
            return send_file(audio_path, as_attachment=True)
        except Exception as e:
            flash(f'Error generating voice: {str(e)}')
            return redirect(url_for('index'))
    else:
        flash('Invalid file type')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)