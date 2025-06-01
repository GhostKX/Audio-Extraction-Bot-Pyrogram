# 🎵 Video to Audio Converter Bot

A **powerful Python-based Telegram bot** that converts MP4 videos to high-quality MP3 audio files. Users can send video files up to **2GB**, and the bot will extract the audio track and deliver a clean MP3 file back to them.

Built using **Pyrogram**, **FFmpeg**, and comprehensive logging, this bot ensures **reliable audio extraction** with detailed activity tracking and error handling.

---

## ✨ Features

### 🎬 Video Processing
- **High-Quality MP3 Audio Extraction** from MP4 videos
- **Supports Large Files** up to 2GB
- **Fast Processing** with FFmpeg integration
- **Automatic File Cleanup** after processing
- **Preserves Original Audio Quality**

### 🔒 Security & Privacy
- **Private Chat Only** - Blocks group/channel usage
- **File Type Validation** - Only accepts MP4 files
- **Size Limit Protection** - Prevents server overload
- **Automatic File Deletion** - No files stored permanently

### 📊 Advanced Logging
- **Comprehensive Activity Tracking**
- **User Interaction Logs**
- **Error Monitoring & Debugging**
- **Performance Metrics** (download/conversion/upload times)
- **File Size Analytics**

### 🛡️ Error Handling
- **Robust Exception Management**
- **User-Friendly Error Messages**
- **Automatic Recovery from Failures**
- **Detailed Error Logging for Debugging**

---

## 🔧 Requirements

### System Dependencies
- **Python 3.8+**
- **FFmpeg** (for audio extraction)
- **Telegram Bot Token**
- **Telegram API Credentials**

### Python Libraries
```
pyrogram==2.0.106
python-dotenv==1.0.0
```

---

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/GhostKX/Audio-Extraction-Bot-Pyrogram.git
cd Audio-Extraction-Bot-Pyrogram
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg

#### Ubuntu/Debian:
```bash
sudo apt update
sudo apt install ffmpeg
```

#### macOS:
```bash
brew install ffmpeg
```

#### Windows:
Download from [FFmpeg official website](https://ffmpeg.org/download.html) and add to PATH.

### 4. Get Telegram Credentials

#### Create a Bot:
1. Message [@BotFather](https://t.me/BotFather) on Telegram
2. Send `/newbot` and follow instructions
3. Save your **Bot Token**

#### Get API Credentials:
1. Visit [my.telegram.org](https://my.telegram.org)
2. Create an application
3. Save your **API ID** and **API Hash**

### 5. Configure Environment Variables

Create a `.env` file in the project root:
```env
API_ID=your_api_id_here
API_HASH=your_api_hash_here
BOT_TOKEN=your_bot_token_here
```

### 6. Run the Bot
```bash
python main.py
```

---

## 📱 Usage

### Starting the Bot
1. Find your bot on Telegram using its username
2. Send `/start` to begin
3. Follow the welcome instructions

### Converting Videos
1. **Send an MP4 video file** to the bot
2. Wait for the **processing confirmation**
3. The bot will:
   - ✅ **Download** your video
   - 🎧 **Extract** the audio track
   - 📤 **Send** you the MP3 file
4. **Receive your audio file!**

### Example Interaction:
```
User: [Sends video.mp4]

Bot: ✅ Processing video: vacation_video.mp4
Bot: 🔍 Downloading the video file: vacation_video.mp4 ...
Bot: 🎧 Extracting audio file: vacation_video.mp4
Bot: ✅ 🎧 Audio extracted successfully.
Bot: 📤 Sending you the extracted audio...
Bot: [Sends vacation_video.mp3] ✅ Here is your MP3 file 🎵
```

---

## 📊 Logging System

The bot creates detailed logs in the `logs/` directory:

### Log Files:
- **`bot_activity.log`** - General bot operations and user interactions
- **Automatic log rotation** when files exceed size limits
- **Timestamped entries** for easy debugging

### What Gets Logged:
- ✅ User start commands and interactions
- 📥 Video upload attempts and validations
- 🎧 Conversion process steps and timing
- ❌ Errors and exceptions with context
- 🚫 Blocked group/channel usage attempts
- 📊 File sizes and processing duration

### Example Log Entry:
```
2024-12-01 15:30:45 - INFO - Received video from user 123456789 (@username) - vacation_video.mp4
2024-12-01 15:30:50 - INFO - Downloaded video for user 123456789: /path/to/video.mp4
2024-12-01 15:31:15 - INFO - Extracted audio for user 123456789: /path/to/audio.mp3
2024-12-01 15:31:20 - INFO - Sent audio to user 123456789
```

---

## 🔒 Security Features

### Access Control
- **Private chats only** - Automatically blocks group/channel usage
- **File type validation** - Only accepts MP4 files
- **File size limits** - Prevents abuse with 2GB maximum

### Privacy Protection
- **Automatic file cleanup** - No user files stored permanently
- **User-specific folders** - Isolated file processing
- **No data persistence** - Files deleted after processing

---

## 🚨 Troubleshooting

### Common Issues:

#### Bot Not Responding:
- ✅ Check if bot token is correct
- ✅ Verify API credentials in `.env`
- ✅ Ensure bot is started with `/start`

#### FFmpeg Errors:
- ✅ Install FFmpeg properly
- ✅ Check FFmpeg is in system PATH
- ✅ Verify video file is not corrupted

#### File Upload Issues:
- ✅ Check file is MP4 format
- ✅ Ensure file is under 2GB
- ✅ Try uploading as document if needed

### Log Analysis:
Check `logs/bot_activity.log` for detailed error information and processing steps.

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Developed by **GhostKX**

- 🌐 **GitHub**: [@GhostKX](https://github.com/GhostKX)
