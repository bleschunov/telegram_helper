import peewee as pw

from telegram_helper.schema.telegram_account_schema import TelegramAccount


def add_telegram_account(alias: str, api_id: int, api_hash: str) -> TelegramAccount:
    try:
        return TelegramAccount.create(alias=alias, api_id=api_id, api_hash=api_hash)
    except pw.IntegrityError:
        raise ValueError(f"Telegram account with alias={alias} already exists.")


def get_telegram_account_by_alias(alias: str) -> TelegramAccount:
    try:
        return TelegramAccount.get(TelegramAccount.alias == alias)
    except pw.DoesNotExist:
        raise ValueError(f"Telegram account with alias={alias} is not found.")


def get_all_telegram_accounts() -> list[TelegramAccount]:
    return list(TelegramAccount.select())
