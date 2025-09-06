import validators
from aiogram import Router
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.types import Message, BotCommand, FSInputFile

from bot.locale import get_text as _
from bot import utils
from bot.cobalt import CobaltAPI

router = Router()

@router.message(CommandStart(deep_link=True))
async def start_cmd(message: Message, command: CommandObject):
    await utils.start_download(message, utils.decode_param(command.args))


@router.message(Command("start"))
async def start_cmd(message: Message):
    commands = [
        BotCommand(command="services", description=_(message, "services_description"))
    ]
    me = await message.bot.get_me()

    await message.bot.set_my_commands(commands)
    await message.answer_photo(
        photo=FSInputFile(f"media/hello_{message.from_user.language_code}.png"),
        caption=_(message, "start_message",
          user=utils.format_name(message.from_user),
          bot_username=me.username
        )
    )

@router.message(Command("services"))
async def services_cmd(message: Message):
    cobalt = CobaltAPI()
    services = cobalt.services()
    await message.answer_photo(
        photo=FSInputFile(f"media/services_{message.from_user.language_code}.png"),
        caption=_(message, "services_message", services=", ".join(services))
    )

@router.message(lambda c: validators.url(c.text))
async def url_message_handle(message: Message):
    print("1: ", message.text)
    await utils.start_download(message)