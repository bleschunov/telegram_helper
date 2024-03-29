from telegram_helper.constant import MAILING_RECEIVERS_SEPARATOR
from telegram_helper.model import telegram_client_model, mailing_list_model
from telegram_helper.service.telegram import send_telegram_message

from telethon.tl.types import Message


def send_message(telegram_account_alias: str, receiver: str, message_text: str) -> Message:
    telegram_account_client = telegram_client_model.get_telegram_client_by_alias(telegram_account_alias)
    with telegram_account_client as c:
        return send_telegram_message(c, receiver, message_text)


def send_messages_to_mailing_list_generator(
    telegram_account_alias,
    mailing_list_alias: str,
    message_text: str
):
    telegram_account_client = telegram_client_model.get_telegram_client_by_alias(telegram_account_alias)
    mailing_list = mailing_list_model.get_mailing_list_by_alias(mailing_list_alias)
    receivers = mailing_list.receivers.split(MAILING_RECEIVERS_SEPARATOR)
    with telegram_account_client as c:
        for receiver in receivers:
            yield lambda: send_telegram_message(c, receiver, message_text)
