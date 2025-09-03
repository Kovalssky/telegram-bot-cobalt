import os

from fluent.runtime import FluentResourceLoader, FluentLocalization
from aiogram.types import Message, User, InlineQuery

DEFAULT_LANG = "ru"

loader = FluentResourceLoader("locales/{locale}")

def get_text(target: Message | User | InlineQuery, locale_text_id: str, **kwargs) -> str:
    locales = os.listdir("locales")
    if isinstance(target, (Message, InlineQuery)):
        locale = target.from_user.language_code
    else:
        locale = target.language_code


    l10n = FluentLocalization(
        locales=[locale if locale in locales else DEFAULT_LANG],
        resource_ids=['messages.ftl', 'errors.ftl'],
        resource_loader=loader,
    )
    result = l10n.format_value(locale_text_id, kwargs)
    return result