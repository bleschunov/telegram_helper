import peewee as pw

from telegram_helper.schema.mailing_list_schema import MailingList


def create_mailing_list(alias: str, receivers: str) -> MailingList:
    try:
        return MailingList.create(alias=alias, receivers=receivers)
    except pw.IntegrityError:
        raise ValueError(f"Mailing list with alias={alias} already exists.")


def get_mailing_list_by_alias(alias: str) -> MailingList:
    try:
        return MailingList.get(MailingList.alias == alias)
    except pw.DoesNotExist:
        raise ValueError(f"Mailing list with alias={alias} is not found.")
