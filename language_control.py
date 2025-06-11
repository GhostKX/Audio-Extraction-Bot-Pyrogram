import json

# Languages dictionary, to easily store and call the text by key
LANGUAGES = {
    'en': {
        'welcome': '''
        🤗 Welcome 😊

        🤖 **Video to Audio Converter Bot** 🎵

        🎬 Send me any video MP4 file
        🎧 I'll extract high-quality MP3 audio from it.

        ⚡️ Supports files up to 2GB
        📌 Preserves audio quality

        ✅ Just send me a video to get started!
        ''',
        'unsupported_type': "❌ Oops! Looks like that's not a video.🤔\n\n😊 Please send me a video file to proceed.",
        'group_block': "🚫 This bot only works in private chats.\n\n💬 Please message me directly.",
        'invalid_format': "🚫 Only MP4 videos are supported.",
        'file_too_large': "🚫 The video is too large (max 2GB allowed).\n\n🎬 Please send a smaller file.",
        'processing': "✅ Processing video: {}",
        'downloading': "🔍 Downloading the video file: {} ...",
        'extracting': "🎧 Extracting audio file: {}",
        'success_extract': "✅ 🎧 Audio extracted successfully.",
        'extract_failed': "❌ Audio extraction failed: {}",
        'sending': "📤 Sending you the extracted audio...",
        'audio_caption': "✅ Here is your MP3 file 🎵",
        'language_prompt': "🌐 Please select your preferred language:",
        'language_set': "🌐 Language set to English",
        'help':'''
        🆘 **How to Use This Bot** 🤖
        
        🎥 **Send me a video file** (MP4 format) 
        🔊 I'll convert it to high-quality MP3 audio
        
        ⚙️ **Features:**
        - Supports videos up to 2GB
        - Preserves original audio quality
        - Fast processing
        
        🌐 **Change language:** /lang
           (Available: English, Русский, O'zbekcha)
        
        📤 Just send me a video and I'll handle the rest!
        '''
    },
    'ru': {
        'welcome': '''
        🤗 Добро пожаловать 😊

        🤖 **Бот для конвертации видео в аудио** 🎵

        🎬 Отправьте мне видео в формате MP4
        🎧 Я извлеку из него аудио в высоком качестве.

        ⚡️ Поддерживаются файлы до 2GB
        📌 Сохраняется качество звука

        ✅ Просто отправьте мне видео, чтобы начать!
        ''',
        'unsupported_type': "❌ Упс! Похоже, это не видео.🤔\n\n😊 Пожалуйста, отправьте мне видеофайл.",
        'group_block': "🚫 Этот бот работает только в личных сообщениях.\n\n💬 Напишите мне напрямую.",
        'invalid_format': "🚫 Поддерживаются только видео в формате MP4.",
        'file_too_large': "🚫 Видео слишком большое (максимум 2GB).\n\n🎬 Пожалуйста, отправьте файл поменьше.",
        'processing': "✅ Обработка видео: {}",
        'downloading': "🔍 Загрузка видеофайла: {} ...",
        'extracting': "🎧 Извлечение аудио: {}",
        'success_extract': "✅ 🎧 Аудио успешно извлечено.",
        'extract_failed': "❌ Ошибка при извлечении аудио: {}",
        'sending': "📤 Отправляю вам извлечённое аудио...",
        'audio_caption': "✅ Ваш MP3 файл 🎵",
        'language_prompt': "🌐 Пожалуйста, выберите язык:",
        'language_set': "🌐 Язык изменён на Русский",
        'help': '''
        🆘 **Как использовать этого бота** 🤖
        
        🎥 **Отправьте мне видеофайл** (формат MP4)
        🔊 Я преобразую его в качественный MP3-аудиофайл
        
        ⚙️ **Возможности:**
        - Поддержка видео до 2GB
        - Сохранение оригинального качества звука
        - Быстрая обработка
        
        🌐 **Сменить язык:** /lang
           (Доступно: English, Русский, O'zbekcha)
        
        📤 Просто отправьте мне видео - я сделаю всё остальное!
        '''
    },
    'uz': {
        'welcome': '''
        🤗 Xush kelibsiz 😊

        🤖 **Video to Audio Converter Bot** 🎵

        🎬 Menga MP4 formatidagi video yuboring
        🎧 Men undan yuqori sifatli MP3 audio ajratib beraman.

        ⚡️ 2GB gacha bo'lgan fayllar qo'llab-quvvatlanadi
        📌 Audio sifatini saqlab qoladi

        ✅ Boshlash uchun menga video yuboring!
        ''',
        'unsupported_type': "❌ Kechirasiz! Bu video emas.🤔\n\n😊 Iltimos, menga video fayl yuboring.",
        'group_block': "🚫 Bu bot faqat shaxsiy xabarlarda ishlaydi.\n\n💬 Menga to'g'ridan-to'g'ri (lichkaga) yozing.",
        'invalid_format': "🚫 Faqat MP4 formatidagi videolar qo'llab-quvvatlanadi.",
        'file_too_large': "🚫 Video juda katta (maksimum 2GB).\n\n🎬 Iltimos, kichikroq fayl yuboring.",
        'processing': "✅ Video tekshirilmoqda: {}",
        'downloading': "🔍 Video fayl yuklab olinmoqda: {} ...",
        'extracting': "🎧 Audio ajratilmoqda: {}",
        'success_extract': "✅ 🎧 Audio muvaffaqiyatli ajratildi.",
        'extract_failed': "❌ Audioni ajratishda xatolik: {}",
        'sending': "📤 Audio fayl sizga yuborilmoqda...",
        'audio_caption': "✅ Sizning MP3 faylingiz 🎵",
        'language_prompt': "🌐 Iltimos, tilni tanlang:",
        'language_set': "🌐 Til O'zbekchaga o'zgartirildi",
        'help': '''
        🆘 **Botdan qanday foydalanish** 🤖
        
        🎥 **Menga video fayl yuboring** (MP4 formatida)
        🔊 Men uni yuqori sifatli MP3 audioga aylantiraman
        
        ⚙️ **Imkoniyatlar:**
        - 2GB gacha bo'lgan videolar
        - Asl audio sifatini saqlab qolish
        - Tez ishlov berish
        
        🌐 **Tilni o'zgartirish:** /lang
           (Mavjud: English, Русский, O'zbekcha)
        
        📤 Shunchaki video yuboring - qolganini men qilaman!
        '''
    }
}

# Creating a new json file that would store user's user_ids to remember users' language preferences
USER_LANGUAGES_FILE = 'user_languages.json'

def load_user_languages():
    try:
        with open(USER_LANGUAGES_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_user_languages(user_languages):
    with open(USER_LANGUAGES_FILE, 'w') as f:
        json.dump(user_languages, f)

def get_user_language(user_id):
    user_languages = load_user_languages()
    return user_languages.get(str(user_id), 'en')  # Default to English

def set_user_language(user_id, lang_code):
    user_languages = load_user_languages()
    user_languages[str(user_id)] = lang_code
    save_user_languages(user_languages)
