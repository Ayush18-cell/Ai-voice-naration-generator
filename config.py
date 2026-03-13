import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-unique-12345')
    ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
    UPLOAD_FOLDER = 'static/audio'
    ALLOWED_EXTENSIONS = {'txt', 'md', 'text', 'csv', 'pdf', 'docx'}
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB max file size
    MAX_TEXT_LENGTH = 50000  # Max characters for text input