import peewee as pw

from telegram_helper.repository.db import db


class BaseModel(pw.Model):
    class Meta:
        database = db
