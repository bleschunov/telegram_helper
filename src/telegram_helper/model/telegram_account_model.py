from telegram_helper.service import telethon
from telegram_helper.repository import telegram_account_repository
from telegram_helper.repository.db import db


def get_all_telegram_accounts():
    return telegram_account_repository.get_all_telegram_accounts()


def get_telegram_account_by_alias(alias: str):
    return telegram_account_repository.get_telegram_account_by_alias(alias)


@db.atomic()
def add_telegram_account(alias: str, api_id: int, api_hash: str):
    telegram_account_db = telegram_account_repository.add_telegram_account(alias, api_id, api_hash)
    client = telethon.get_telegram_client(
        telegram_account_db.alias,
        telegram_account_db.api_id,
        telegram_account_db.api_hash
    )
    client.start()
    return telegram_account_db
