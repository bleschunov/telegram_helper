import peewee as pw

from telegram_helper.schema.base_model import BaseModel


class MailingList(BaseModel):
    id = pw.IntegerField(primary_key=True)
    alias = pw.CharField(null=False, unique=True, index=True)
    receivers = pw.CharField(null=False, max_length=1)

    class Meta:
        table_name = "mailing_list"

    def __str__(self) -> str:
        return f"{self.id}, {self.alias}"
