from telegram_helper.schema.telegram_account_schema import TelegramAccount


def add_telegram_account(alias: str, api_id: int, api_hash: str) -> TelegramAccount:
    return TelegramAccount.create(alias=alias, api_id=api_id, api_hash=api_hash)


def get_telegram_account_by_alias(alias: str) -> TelegramAccount:
    try:
        return TelegramAccount.get(TelegramAccount.alias == alias)
    except TelegramAccount.DoesNotExist as e:
        raise ValueError(f"Telegram account with alias={alias} is not found.")


def get_all_telegram_accounts() -> list[TelegramAccount]:
    return list(TelegramAccount.select())
