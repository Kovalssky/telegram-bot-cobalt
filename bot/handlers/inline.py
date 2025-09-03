import validators
from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

from bot.locale import get_text as _
from bot import utils

router = Router()

@router.inline_query()
async def inline_handler(query: InlineQuery):
    encoded = utils.encode_param(query.query)
    user_input = query.query
    results = []
    switch_param = encoded

    if not validators.url(user_input):
        results = [
            InlineQueryResultArticle(
                id="1",
                title=_(query, "error_invalid_url"),
                input_message_content=InputTextMessageContent(
                    message_text=_(query, "inline_alert")
                )
            )
        ]

    try:
        await query.answer(
            results=results,
            switch_pm_text=_(query, "inline_btn"),
            switch_pm_parameter=switch_param,
            is_personal=True,
            cache_time=0
        )
    except:
        pass