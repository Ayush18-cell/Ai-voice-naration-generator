# AI Voice Narration Generator

A modern web application that converts text into lifelike speech using Google Text-to-Speech (gTTS) and ElevenLabs AI voices. Supports text input, file uploads (TXT, MD, CSV, PDF, DOCX), and features a beautiful dark mode interface.

## 🎤 Features

- **Dual TTS Engines**: Choose between free Google TTS or premium ElevenLabs voices
- **Multiple Input Methods**: Enter text directly or upload files
- **File Format Support**: TXT, Markdown, CSV, PDF, and DOCX files
- **Smart Text Processing**: Automatic text extraction from documents and chunking for long content
- **Modern UI**: Responsive design with dark/light mode toggle
- **Audio Download**: Generated speech saved as MP3 files
- **Large File Support**: Up to 50MB file uploads and 50,000 character text limits

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. **Clone or download the project**
   ```bash
   cd "AI Voice Narration Generator"
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   # source venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   SECRET_KEY=your-unique-secret-key-here
   ELEVENLABS_API_KEY=your-elevenlabs-api-key-here
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## 📖 Usage

### Web Interface
1. **Text Input**: Type or paste text directly into the textarea
2. **File Upload**: Click "Choose File" to upload supported document formats
3. **Voice Selection**:
   - **Google TTS**: Free, no API key required
   - **ElevenLabs**: Premium AI voices (requires API key)
4. **Generate**: Click the button to create audio
5. **Download**: Audio file downloads automatically

### Voice Options
- **Google TTS**: Standard text-to-speech with natural pronunciation
- **ElevenLabs**: High-quality AI voices with emotional expression
  - Requires ElevenLabs API key
  - Supports custom voice IDs

## ⚙️ Configuration

### Environment Variables
- `SECRET_KEY`: Flask session secret (generate a random string)
- `ELEVENLABS_API_KEY`: Your ElevenLabs API key (optional for gTTS-only use)

### File Limits
- **Upload Size**: 50MB maximum
- **Text Length**: 50,000 characters maximum
- **Audio Format**: MP3 output

## 📁 Supported File Types

| Format | Description | Text Extraction |
|--------|-------------|-----------------|
| .txt   | Plain text  | Direct reading  |
| .md    | Markdown    | Direct reading  |
| .csv   | CSV files   | Direct reading  |
| .pdf   | PDF documents| PyPDF2 extraction|
| .docx  | Word documents| python-docx extraction|

## 🔑 API Keys

### ElevenLabs Setup
1. Sign up at [ElevenLabs](https://elevenlabs.io)
2. Get your API key from the dashboard
3. Add it to your `.env` file
4. Use voice IDs from your ElevenLabs account

### Google TTS
No API key required - works out of the box!

## 🛠️ Development

### Project Structure
```
AI Voice Narration Generator/
├── app.py                 # Main Flask application
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── services/
│   ├── voice_generator.py # TTS service logic
│   └── audio_generator.py # Audio processing utilities
├── static/
│   ├── css/style.css      # Styling and themes
│   └── js/script.js       # Frontend JavaScript
├── templates/
│   └── index.html         # Main web interface
├── utils/
│   └── file_handler.py    # File processing utilities
└── uploads/               # Temporary upload directory
```

### Adding New Features
- Voice engines in `services/voice_generator.py`
- UI components in `templates/index.html`
- Styling in `static/css/style.css`
- File handlers in `utils/file_handler.py`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source. Feel free to use and modify as needed.

## 🆘 Troubleshooting

### Common Issues
- **"Voice ID is required"**: Select ElevenLabs and provide a valid voice ID
- **"File too large"**: Reduce file size or contact support for limit increases
- **"API key invalid"**: Check your ElevenLabs API key in `.env`
- **"Text extraction failed"**: Ensure PDF/DOCX contains selectable text (not images)

### Getting Help
- Check the browser console for errors
- Verify all dependencies are installed
- Ensure `.env` file exists with correct values

## 🎯 Future Enhancements

- [ ] Voice cloning capabilities
- [ ] Batch processing for multiple files
- [ ] Audio editing and effects
- [ ] Multi-language support
- [ ] Voice preview before generation
- [ ] Integration with more TTS providers

---

**Enjoy creating amazing voice narrations! 🎵**
