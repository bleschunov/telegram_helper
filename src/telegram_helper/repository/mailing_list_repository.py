from telegram_helper.schema.mailing_list_schema import MailingList


def create_mailing_list(alias: str, receivers: str) -> MailingList:
    return MailingList.create(alias=alias, receivers=receivers)


def get_mailing_list_by_alias(alias: str) -> list[MailingList]:
    try:
        return MailingList.get(MailingList.alias == alias)
    except MailingList.DoesNotExist:
        raise ValueError(f"Mailing list with alias={alias} is not found.")
