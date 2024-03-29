from typing import Literal

from telethon import TelegramClient
from telethon.tl.types import Message


async def send_telegram_message(
        telegram_client: TelegramClient,
        receiver: str | int | Literal["me"],
        message_text: str
) -> Message:
    """
    Method to send telegram message from specific telegram account to specific user.

    Args:
        telegram_client: Telethon client of specific account.
        receiver: ID, phone number or handle of receiver.
        message_text: Message content.

    Returns:
        Message: Message object from Telethon library.
    """
    return await telegram_client.send_message(receiver, message_text)
