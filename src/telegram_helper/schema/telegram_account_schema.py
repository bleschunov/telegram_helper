import peewee as pw

from telegram_helper.schema.base_model import BaseModel


class TelegramAccount(BaseModel):
    id = pw.IntegerField(primary_key=True)
    alias = pw.CharField(null=False)
    api_id = pw.IntegerField(null=False)
    api_hash = pw.CharField(null=False)

    class Meta:
        table_name = "telegram_account"

    def __str__(self) -> str:
        return f"{self.id}, {self.alias}"
