from telegram_helper.repository.db import db
from telegram_helper.schema.telegram_account_schema import TelegramAccount


def init_db():
    db.connect()
    db.create_tables([TelegramAccount])
