# 🎵 Video to Audio Converter Bot

<div align="center">

[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-0088CC?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![Pyrogram](https://img.shields.io/badge/Pyrogram-2.0+-FF6B6B?style=for-the-badge&logo=telegram&logoColor=white)](https://pyrogram.org)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-Audio%20Processing-007808?style=for-the-badge&logo=ffmpeg&logoColor=white)](https://ffmpeg.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**A powerful Python-based Telegram bot that converts MP4 videos to high-quality MP3 audio files. Users can send video files up to 2GB, and the bot will extract the audio track and deliver a clean MP3 file back to them.**

Built using **Pyrogram**, **FFmpeg**, and comprehensive logging, this bot ensures **reliable audio extraction** with detailed activity tracking and error handling.

[🚀 Quick Start](#-installation) • [✨ Features](#-features) • [📱 Usage](#-usage) • [🔧 Configuration](#-configuration) • [🚨 Troubleshooting](#-troubleshooting)

---

</div>

## 🎯 Overview

Transform your video content into high-quality audio files with this sophisticated Telegram bot. Built with **Pyrogram** and **FFmpeg**, it handles files up to **2GB** while maintaining exceptional audio quality and providing a seamless user experience across multiple languages.

### 🏆 **Why Choose This Bot?**
- **🎧 Premium Audio Quality** - Preserves original audio fidelity
- **🌍 Multilingual Support** - English, Russian, and Uzbek interfaces
- **📊 Enterprise Logging** - Comprehensive activity tracking
- **🔒 Privacy-First Design** - Automatic file cleanup and secure processing
- **⚡ Lightning Fast** - Optimized FFmpeg processing pipeline

---

## ✨ Features

### 🎬 **Video Processing**
<table>
<tr>
<th width="25%">🎯 Feature</th>
<th width="25%">🎵 Audio Quality</th>
<th width="25%">📁 File Handling</th>
<th width="25%">⚡ Performance</th>
</tr>
<tr>
<td><strong>Format Support</strong></td>
<td>Original Quality Preservation</td>
<td>Up to 2GB Files</td>
<td>Optimized Processing</td>
</tr>
<tr>
<td><strong>Processing</strong></td>
<td>High-Quality MP3 Output</td>
<td>MP4 Video Input</td>
<td>Fast FFmpeg Integration</td>
</tr>
<tr>
<td><strong>Cleanup</strong></td>
<td>No Quality Loss</td>
<td>Automatic File Deletion</td>
<td>Memory Efficient</td>
</tr>
<tr>
<td><strong>Validation</strong></td>
<td>Audio Track Verification</td>
<td>File Type Checking</td>
<td>Size Limit Protection</td>
</tr>
</table>

- **High-Quality MP3 Audio Extraction** from MP4 videos
- **Supports Large Files** up to 2GB
- **Fast Processing** with FFmpeg integration
- **Automatic File Cleanup** after processing
- **Preserves Original Audio Quality**

### 🌐 **Multilingual Support**

| Language | Flag | Coverage | Persistence |
|----------|------|----------|-------------|
| **English** | 🇬🇧 | Complete Interface | ✅ Saved |
| **Russian** | 🇷🇺 | Full Localization | ✅ Saved |
| **Uzbek** | 🇺🇿 | Native Support | ✅ Saved |

**Features:**
- **3 Languages Supported**: English 🇬🇧, Russian 🇷🇺, Uzbek 🇺🇿
- **Persistent Language Preferences** - Bot remembers your choice
- **Dynamic Language Switching** with `/lang` command
- **Localized User Interface** - All messages in your preferred language

### 🔒 **Security & Privacy**

#### **Access Control**
- **Private Chat Only** - Blocks group/channel usage
- **File Type Validation** - Only accepts MP4 files
- **Size Limit Protection** - Prevents server overload
- **Automatic File Deletion** - No files stored permanently

#### **Privacy Protection**
- **User-specific Folders** - Isolated file processing
- **No Data Persistence** - Files deleted after processing
- **Language Preferences Only** - Only user language choice is stored locally

### 📊 **Advanced Logging**
- **Comprehensive Activity Tracking**
- **User Interaction Logs**
- **Error Monitoring & Debugging**
- **Performance Metrics** (download/conversion/upload times)
- **File Size Analytics**

### 🛡️ **Error Handling**
- **Robust Exception Management**
- **User-Friendly Error Messages**
- **Automatic Recovery from Failures**
- **Detailed Error Logging for Debugging**

---

## 🔧 Requirements

### **System Dependencies**
| Component | Minimum | Recommended | Purpose |
|-----------|---------|-------------|---------|
| **Python** | 3.8+ | 3.10+ | Core runtime |
| **FFmpeg** | Latest | Latest | Audio processing |
| **RAM** | 1GB | 2GB+ | File processing |
| **Storage** | 5GB | 10GB+ | Temporary files |
| **Network** | 10 Mbps | 50+ Mbps | File transfers |

### **Python Libraries**
```
pyrogram==2.0.106
python-dotenv==1.0.0
```

### **External Services**
- **Telegram Bot Token** - From [@BotFather](https://t.me/BotFather)
- **Telegram API Credentials** - From [my.telegram.org](https://my.telegram.org)

---

## 🚀 Installation

### **1. Clone the Repository**
```bash
git clone https://github.com/GhostKX/Audio-Extraction-Bot-Pyrogram.git
cd Audio-Extraction-Bot-Pyrogram
```

### **2. Install Dependencies**
```bash
# Create virtual environment (recommended)
python -m venv audio_bot_env
source audio_bot_env/bin/activate  # Linux/Mac
audio_bot_env\Scripts\activate     # Windows

# Install Python packages
pip install -r requirements.txt
```

### **3. Install FFmpeg**

#### **Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

#### **macOS:**
```bash
brew install ffmpeg
```

#### **Windows:**
Download from [FFmpeg official website](https://ffmpeg.org/download.html) and add to PATH.

#### **Verify FFmpeg:**
```bash
ffmpeg -version
```

### **4. Get Telegram Credentials**

#### **Create a Bot:**
1. Message [@BotFather](https://t.me/BotFather) on Telegram
2. Send `/newbot` and follow instructions
3. Save your **Bot Token**

#### **Get API Credentials:**
1. Visit [my.telegram.org](https://my.telegram.org)
2. Create an application
3. Save your **API ID** and **API Hash**

### **5. Configure Environment Variables**

Create a `.env` file in the project root:
```env
API_ID=your_api_id_here
API_HASH=your_api_hash_here
BOT_TOKEN=your_bot_token_here
```

### **6. Run the Bot**
```bash
python main.py
```

**Expected output:**
```
✅ Bot started successfully!
📱 Bot username: @your_bot_username
🎵 Ready to convert videos to audio!
```

---

## 📱 Usage

### **Starting the Bot**
1. Find your bot on Telegram using its username
2. Send `/start` to begin
3. Follow the welcome instructions

### **Available Commands**

| Command | Description | Example |
|---------|-------------|---------|
| `/start` | Initialize the bot and see welcome message | Start conversation |
| `/help` | Get detailed usage instructions | Get help anytime |
| `/lang` | Change language preference | Switch to Russian/Uzbek |

### **Language Selection**
The bot supports multiple languages with persistent preferences:

1. **First time users** - Bot defaults to English
2. **Change language** - Use `/lang` command anytime
3. **Language options**:
   - 🇬🇧 **English** - Full interface in English
   - 🇷🇺 **Русский** - Complete Russian localization
   - 🇺🇿 **O'zbekcha** - Full Uzbek language support
4. **Persistent storage** - Your language choice is remembered across sessions

#### **Switching Languages:**
```
User: /lang
Bot: 🌍 Choose your language:
     🇬🇧 English
     🇷🇺 Русский  
     🇺🇿 O'zbekcha
User: [Selects Russian]
Bot: ✅ Язык изменен на русский!
```

### **Converting Videos**
1. **Send an MP4 video file** to the bot
2. Wait for the **processing confirmation**
3. The bot will:
   - ✅ **Download** your video
   - 🎧 **Extract** the audio track
   - 📤 **Send** you the MP3 file
4. **Receive your audio file!**

### **Example Interaction:**
```
User: [Sends vacation_video.mp4 - 150MB]

Bot: ✅ Processing video: vacation_video.mp4
Bot: 🔍 Downloading the video file: vacation_video.mp4 ...
Bot: 🎧 Extracting audio file: vacation_video.mp4
Bot: ✅ 🎧 Audio extracted successfully.
Bot: 📤 Sending you the extracted audio...
Bot: [Sends vacation_video.mp3 - 12MB] ✅ Here is your MP3 file 🎵

Processing time: 45 seconds
File size reduction: 92%
```

### **File Requirements**

#### **Supported Formats:**
- ✅ **Input:** MP4 video files only
- ✅ **Output:** High-quality MP3 audio
- ✅ **Maximum size:** 2GB (2,147,483,648 bytes)
- ✅ **Audio codecs:** All FFmpeg-supported codecs

#### **Quality Specifications:**
- 🎵 **Audio Quality:** Preserves original bitrate
- 📊 **Sample Rate:** Maintains source sample rate
- 🔊 **Channels:** Stereo/Mono preserved
- 💾 **Compression:** Optimized MP3 encoding

---

## 🔧 Configuration

### **Environment Variables**

Create a `.env` file with the following configuration:

```env
# Required: Telegram Bot Configuration
BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
API_ID=12345678
API_HASH=abcdef1234567890abcdef1234567890

# Optional: Bot Settings
LOG_LEVEL=INFO                    # DEBUG, INFO, WARNING, ERROR
MAX_FILE_SIZE=2147483648         # Maximum file size in bytes (2GB)
TEMP_DIR=./temp                  # Temporary files directory
LOGS_DIR=./logs                  # Logs directory

# Optional: FFmpeg Settings
FFMPEG_PATH=ffmpeg               # Custom FFmpeg path if needed
AUDIO_BITRATE=192k              # Output audio bitrate
```

### **File Structure:**
```
Audio-Extraction-Bot-Pyrogram/
├── main.py                      # Main bot application
├── .env                         # Environment configuration
├── requirements.txt             # Python dependencies
├── user_languages.json          # User language preferences
├── logs/                        # Log files directory
│   └── bot_activity.log        # Main activity log
├── temp/                        # Temporary processing files
│   └── user_folders/           # User-specific temp folders
└── README.md                   # This documentation
```

---

## 📊 Logging System

The bot creates detailed logs in the `logs/` directory:

### **Log Files:**
- **`bot_activity.log`** - General bot operations and user interactions
- **Automatic log rotation** when files exceed size limits
- **Timestamped entries** for easy debugging

### **What Gets Logged:**
- ✅ User start commands and interactions
- 🌐 Language preference changes
- 📥 Video upload attempts and validations
- 🎧 Conversion process steps and timing
- ❌ Errors and exceptions with context
- 🚫 Blocked group/channel usage attempts
- 📊 File sizes and processing duration

### **Example Log Entry:**
```
2024-12-01 15:30:45 - INFO - Received video from user 123456789 (@username) - vacation_video.mp4
2024-12-01 15:30:50 - INFO - Downloaded video for user 123456789: /path/to/video.mp4
2024-12-01 15:31:15 - INFO - Extracted audio for user 123456789: /path/to/audio.mp3
2024-12-01 15:31:20 - INFO - Sent audio to user 123456789
```

### **Performance Monitoring:**
- ⏱️ **Processing Duration** - Download, conversion, upload times
- 📊 **File Size Analytics** - Input/output size comparisons
- 💾 **Memory Usage** - Resource consumption tracking
- 🔄 **Success Rates** - Conversion success statistics

---

## 📈 Performance Metrics

### **Typical Performance Benchmarks**

| Video Size | Audio Size | Download Time | Conversion Time | Upload Time | Total Time |
|------------|------------|---------------|-----------------|-------------|------------|
| 10 MB | 800 KB | 2-5 sec | 3-8 sec | 1-2 sec | 6-15 sec |
| 50 MB | 4 MB | 8-15 sec | 12-25 sec | 3-6 sec | 23-46 sec |
| 100 MB | 8 MB | 15-30 sec | 25-45 sec | 5-10 sec | 45-85 sec |
| 500 MB | 40 MB | 60-120 sec | 90-180 sec | 20-40 sec | 170-340 sec |
| 1 GB | 80 MB | 120-240 sec | 180-300 sec | 40-60 sec | 340-600 sec |
| 2 GB | 160 MB | 240-480 sec | 300-600 sec | 60-120 sec | 600-1200 sec |

**Note:** Times vary based on internet connection, server load, and file complexity.

### **Optimization Features**
- ⚡ **Parallel Processing** - Simultaneous download and conversion preparation
- 💾 **Memory Efficient** - Streaming file processing
- 🔄 **Smart Cleanup** - Automatic temporary file removal
- 📊 **Quality Optimization** - Balanced size and quality output

---

## 🚨 Troubleshooting

### **Common Issues:**

#### **Bot Not Responding:**
- ✅ Check if bot token is correct
- ✅ Verify API credentials in `.env`
- ✅ Ensure bot is started with `/start`

```bash
# Check bot token
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('Token:', os.getenv('BOT_TOKEN')[:10] + '...')"

# Verify API credentials
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('API ID:', os.getenv('API_ID')); print('API Hash:', os.getenv('API_HASH')[:10] + '...')"
```

#### **Language Issues:**
- ✅ Use `/lang` command to change language
- ✅ Check if `user_languages.json` file is writable
- ✅ Restart bot if language settings don't persist

```bash
# Check user_languages.json permissions
ls -la user_languages.json
chmod 644 user_languages.json

# Reset language file if corrupted
echo '{}' > user_languages.json
```

#### **FFmpeg Errors:**
- ✅ Install FFmpeg properly
- ✅ Check FFmpeg is in system PATH
- ✅ Verify video file is not corrupted

```bash
# Verify FFmpeg installation
ffmpeg -version

# Test FFmpeg with sample conversion
ffmpeg -f lavfi -i testsrc2=duration=1:size=320x240:rate=1 -f lavfi -i sine=frequency=1000:duration=1 -c:v libx264 -c:a aac -shortest test_input.mp4
ffmpeg -i test_input.mp4 -q:a 0 -map a test_output.mp3
```

#### **File Upload Issues:**
- ✅ Check file is MP4 format
- ✅ Ensure file is under 2GB
- ✅ Try uploading as document if needed

```bash
# Verify file format
file your_video.mp4
ffprobe -v quiet -print_format json -show_format your_video.mp4

# Check temporary directory permissions
ls -la temp/
mkdir -p temp
chmod 755 temp
```

### **Log Analysis:**
Check `logs/bot_activity.log` for detailed error information and processing steps.

```bash
# Find recent errors
grep -i error logs/bot_activity.log | tail -10

# Check conversion times
grep -i "conversion completed" logs/bot_activity.log | tail -5

# Monitor user activity
grep -i "user.*started" logs/bot_activity.log | tail -10
```

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### **License Summary**
- ✅ **Commercial use** - Use in commercial projects
- ✅ **Modification** - Modify and adapt the code
- ✅ **Distribution** - Distribute original or modified versions
- ✅ **Private use** - Use privately without restrictions
- ❗ **Liability** - No warranty or liability provided
- ❗ **Attribution** - Include original license and copyright

---

<div align="center">

## 👨‍💻 Author

Developed by **GhostKX**

**GitHub**: [@GhostKX](https://github.com/GhostKX)

</div>