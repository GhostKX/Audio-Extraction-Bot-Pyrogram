import os
import re
import asyncio
import subprocess
import logging

from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from language_control import LANGUAGES, get_user_language, set_user_language



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
    lang = get_user_language(user.id)
    await message.reply_text(LANGUAGES[lang]['welcome'])


@app.on_message(filters.command(['lang']))
async def set_language(client: Client, message: Message):
    keyboard = [
        [InlineKeyboardButton("English 🇬🇧", callback_data="lang_en")],
        [InlineKeyboardButton("Русский 🇷🇺", callback_data="lang_ru")],
        [InlineKeyboardButton("O'zbekcha 🇺🇿", callback_data="lang_uz")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Get user's current language for the prompt
    current_lang = get_user_language(message.from_user.id)
    prompt = LANGUAGES[current_lang]['language_prompt']

    await message.reply_text(prompt, reply_markup=reply_markup)


@app.on_message(filters.command(['help']))
async def help_bot(client: Client, message: Message):
    user = message.from_user
    logging.info(f"/help command from user {user.id}")
    lang = get_user_language(user.id)
    await message.reply_text(LANGUAGES[lang]['help'])


@app.on_callback_query(filters.regex(r'^lang_'))
async def handle_language_selection(client: Client, callback_query: CallbackQuery):
    lang_code = callback_query.data.split('_')[1]  # Extract 'en', 'ru', or 'uz'
    user_id = callback_query.from_user.id

    if lang_code not in LANGUAGES:
        await callback_query.answer("Invalid language selection")
        return

    set_user_language(user_id, lang_code)
    await callback_query.message.edit_text(LANGUAGES[lang_code]['language_set'])
    await callback_query.answer()


@app.on_message(filters.private & ~filters.video & ~filters.command(['start', 'lang', 'help']))
async def handling_messages(client: Client, message: Message):
    user = message.from_user
    logging.info(f"Unsupported message type from user {user.id} (@{user.username or 'N/A'}): {message.text or 'non-text content'}")
    lang = get_user_language(user.id)
    await message.reply_text(LANGUAGES[lang]['unsupported_type'])


@app.on_message(~filters.private)
async def handling_groups_channels(client: Client, message: Message):
    user = message.from_user
    logging.info(f"Blocked group/channel message from user {user.id} (@{user.username or 'N/A'}) in chat {message.chat.id}")
    lang = get_user_language(user.id)
    await message.reply_text(LANGUAGES[lang]['group_block'])

# Function to check the filename is valid or not
def sanitize_filename(filename):
    return re.sub(r'[^\w\-_\. ]', '_', filename)

@app.on_message(filters.private & filters.video)
async def handling_video(client: Client, message: Message):
    user = message.from_user
    chat_id = message.chat.id
    lang = get_user_language(user.id)

    if message.video.mime_type != "video/mp4" or not message.video.file_name.lower().endswith(".mp4"):
        await message.reply_text(LANGUAGES[lang]['invalid_format'])
        logging.warning(f"User {user.id} sent unsupported file type: {message.video.file_name}")
        return

    if message.video.file_size > 2 * 1024 * 1024 * 1024:
        await message.reply_text(LANGUAGES[lang]['file_too_large'])
        logging.warning(f"User {user.id} sent a file exceeding 2GB: {message.video.file_name}")
        return

    logging.info(f"Received video from user {user.id} (@{user.username or 'N/A'}) - {message.video.file_name}")
    bot_message = await message.reply_text(LANGUAGES[lang]['processing'].format(message.video.file_name))

    safe_file_name = sanitize_filename(message.video.file_name)
    video_file_name = f"{safe_file_name}_{message.video.file_unique_id}.mp4"

    user_file = os.path.join(media_files, f'{message.from_user.id}')
    os.makedirs(media_files, exist_ok=True)

    video_path = os.path.join(user_file, video_file_name)

    await bot_message.edit_text(LANGUAGES[lang]['downloading'].format(message.video.file_name))

    downloaded_file_path = await message.download(file_name=video_path)
    logging.info(f"Downloaded video for user {user.id}: {downloaded_file_path}")

    await bot_message.edit_text(LANGUAGES[lang]['extracting'].format(message.video.file_name))

    audio_file_name = f'{safe_file_name}_{message.video.file_unique_id}.mp3'
    audio_path = os.path.join(user_file, audio_file_name)
    try:
        # Main code part actually extracts the audio from the video files and saves it in the mp3 file
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
        await bot_message.edit_text(LANGUAGES[lang]['success_extract'])

    except Exception as e:

        logging.error(f"Audio extraction failed for user {user.id}: {e}")
        await bot_message.edit_text(LANGUAGES[lang]['extract_failed'].format(message.video.file_name))

        if os.path.exists(downloaded_file_path):
            os.remove(downloaded_file_path)
        if os.path.exists(audio_path):
            os.remove(audio_path)
        return

    await bot_message.edit_text(LANGUAGES[lang]['sending'])

    await app.send_audio(chat_id, audio_path, caption=f"{LANGUAGES[lang]['audio_caption']}")
    logging.info(f"Sent audio to user {user.id}")

    await bot_message.delete()

    os.remove(downloaded_file_path)
    os.remove(audio_path)


if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
    print("Bot stopped.")