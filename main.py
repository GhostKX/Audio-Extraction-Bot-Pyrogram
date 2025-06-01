import os
import re
import asyncio
import subprocess
import logging

from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv


# Logging configuration
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "bot_activity.log")

logging.basicConfig(
    filename=log_file,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# --- Bot Configuration ---
# Load environment variables from .env file
load_dotenv()
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Create the bot client
app = Client(
    "video_echo_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

media_files = 'users_media'
os.makedirs(media_files, exist_ok=True)

@app.on_message(filters.command(['start']))
async def start_bot(client: Client, message: Message):
    user = message.from_user
    logging.info(f"/start command from user {user.id} (@{user.username or 'N/A'})")
    welcome_text = '''
    🤗 Welcome 😊
    
    🤖 **Video to Audio Converter Bot** 🎵

    🎬 Send me any video MP4 file
    🎧I'll extract high-quality MP3 audio from it.
    
    ⚡️Supports files up to 2GB
    📌 Preserves audio quality
    
    ✅ Just send me a video to get started!
    '''
    await message.reply_text(welcome_text)


@app.on_message(filters.private & ~filters.video & ~filters.command(['start']))
async def handling_messages(client: Client, message: Message):
    user = message.from_user
    logging.info(f"Unsupported message type from user {user.id} (@{user.username or 'N/A'}): {message.text or 'non-text content'}")
    await message.reply_text(
        "❌ Oops! Looks like that's not a video.🤔\n\n"
        "😊 Please send me a video file to proceed."
    )

@app.on_message(~filters.private)
async def handling_groups_channels(client: Client, message: Message):
    user = message.from_user
    logging.info(f"Blocked group/channel message from user {user.id} (@{user.username or 'N/A'}) in chat {message.chat.id}")
    await message.reply_text("🚫 This bot only works in private chats.\n\n"
                             "💬 Please message me directly.")


def sanitize_filename(filename):
    return re.sub(r'[^\w\-_\. ]', '_', filename)

@app.on_message(filters.private & filters.video)
async def handling_video(client: Client, message: Message):
    user = message.from_user
    chat_id = message.chat.id

    if message.video.mime_type != "video/mp4" or not message.video.file_name.lower().endswith(".mp4"):
        await message.reply_text("🚫 Only MP4 videos are supported.")
        logging.warning(f"User {user.id} sent unsupported file type: {message.video.file_name}")
        return

    if message.video.file_size > 2 * 1024 * 1024 * 1024:
        await message.reply_text("🚫 The video is too large (max 2GB allowed).\n\n"
                                 "🎬 Please send a smaller file.")
        logging.warning(f"User {user.id} sent a file exceeding 2GB: {message.video.file_name}")
        return

    logging.info(f"Received video from user {user.id} (@{user.username or 'N/A'}) - {message.video.file_name}")
    bot_message = await message.reply_text(f"✅ Processing video: {message.video.file_name}")

    safe_file_name = sanitize_filename(message.video.file_name)
    video_file_name = f"{safe_file_name}_{message.video.file_unique_id}.mp4"

    user_file = os.path.join(media_files, f'{message.from_user.id}')
    os.makedirs(media_files, exist_ok=True)

    video_path = os.path.join(user_file, video_file_name)

    await bot_message.edit_text(f"🔍 Downloading the video file: {message.video.file_name} ...")
    downloaded_file_path = await message.download(file_name=video_path)
    logging.info(f"Downloaded video for user {user.id}: {downloaded_file_path}")

    await bot_message.edit_text(f"🎧Extracting audio file: {message.video.file_name}")

    audio_file_name = f'{safe_file_name}_{message.video.file_unique_id}.mp3'
    audio_path = os.path.join(user_file, audio_file_name)
    try:
        subprocess.run([
            'ffmpeg',
            '-i', downloaded_file_path,
            '-vn',
            '-acodec', 'libmp3lame',
            '-y',
            audio_path,
        ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        logging.info(f"Extracted audio for user {user.id}: {audio_path}")
        await bot_message.edit_text('✅ 🎧 Audio extracted successfully.')
    except Exception as e:
        logging.error(f"Audio extraction failed for user {user.id}: {e}")
        await bot_message.edit_text(f"❌ Audio extraction failed: {e}")
        if os.path.exists(downloaded_file_path):
            os.remove(downloaded_file_path)
        if os.path.exists(audio_path):
            os.remove(audio_path)
        return


    await bot_message.edit_text("📤 Sending you the extracted audio...")
    await app.send_audio(chat_id, audio_path, caption="✅ Here is your MP3 file 🎵")
    logging.info(f"Sent audio to user {user.id}")

    await bot_message.delete()

    os.remove(downloaded_file_path)
    os.remove(audio_path)

if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
    print("Bot stopped.")