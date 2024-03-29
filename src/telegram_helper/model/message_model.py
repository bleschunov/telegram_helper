from telegram_helper.repository import telegram_account_repository
from telegram_helper.service.telegram import send_telegram_message
from telegram_helper.service.telethon import get_telegram_client

from telethon.tl.types import Message


async def send_message(alias: str, receiver: str, message_text: str) -> Message:
    telegram_account_db = telegram_account_repository.get_telegram_account_by_alias(alias)
    telegram_account_client = get_telegram_client(
        telegram_account_db.alias,
        telegram_account_db.api_id,
        telegram_account_db.api_hash
    )
    async with telegram_account_client as c:
        return await send_telegram_message(c, receiver, message_text)
