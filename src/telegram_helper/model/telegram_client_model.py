from telegram_helper.repository import telegram_account_repository
from telegram_helper.service.telethon import get_telegram_client


def get_telegram_client_by_alias(alias: str, ):
    telegram_account_db = telegram_account_repository.get_telegram_account_by_alias(alias)
    return get_telegram_client(
        telegram_account_db.alias,
        telegram_account_db.api_id,
        telegram_account_db.api_hash
    )
