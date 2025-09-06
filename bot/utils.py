import base64
import os

from aiogram.types import User, Message, FSInputFile

from bot.locale import get_text as _
from bot.cobalt import CobaltAPI
from bot import log

VIDEO_FORMATS = [
    "mp4", "mov", "avi", "wmv", "flv", "mkv", "webm", "mpeg", "3gp", "ts",
    "m4v", "mpg", "vob", "ogv", "m2ts"
]

PHOTO_FORMATS = [
    "jpg", "jpeg", "png", "gif", "bmp", "tiff", "svg", "heic", "webp"
]

AUDIO_FORMATS = [
    "mp3", "wav", "aac", "flac", "ogg", "m4a", "wma", "alac"
]


def format_name(user: User) -> str:
    if user.username:
        return f"@{user.username}"
    return f"<a href=\"tg://user?id={user.id}\">{user.first_name}</a>"

async def answer(filename: str, message: Message, url: str):
    extension = filename.split(".")[-1]
    if extension in VIDEO_FORMATS:
        await message.answer_video(
            FSInputFile(filename),
            caption=_(
                message, "video_downloaded",
                url=url
            )
        )
    elif extension in PHOTO_FORMATS:
        await message.answer_photo(
            FSInputFile(filename),
            caption=_(
                message, "photo_downloaded",
                url=url
            )
        )
    elif extension in AUDIO_FORMATS:
        await message.answer_audio(
            FSInputFile(filename),
            caption=_(
                message, "audio_downloaded",
                url=url
            )
        )
    os.remove(filename)

def encode_param(text: str) -> str:
    encoded = base64.urlsafe_b64encode(text.encode()).decode()
    return encoded.rstrip("=")

def decode_param(encoded: str) -> str:
    padding = '=' * (-len(encoded) % 4)
    decoded = base64.urlsafe_b64decode(encoded + padding).decode()
    return decoded

async def start_download(message: Message, link: str = None):
    cobalt = CobaltAPI()
    url = link if link else message.text
    print("2: ", url)
    m = await message.answer(_(message, "wait_message", url=url))
    if "/start" in message.text:
        await message.delete()
    filename = cobalt.download(url)
    if not filename:
        await m.edit_text(_(message, "error_url"))
        log.error(filename)
        return
    await answer(filename, m, url=url)
    await m.delete()
