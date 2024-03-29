from pathlib import Path

from telegram_helper.constant import MAILING_RECEIVERS_SEPARATOR
from telegram_helper.repository import mailing_list_repository
from telegram_helper.schema.mailing_list_schema import MailingList


def extract_receivers_from_file(file_path: Path) -> list[str]:
    with open(file_path, "r") as r:
        return r.readlines()


def create_mailing_list(alias: str, receivers: list[str]) -> MailingList:
    def _remove_empty_receivers(x: str):
        return len(x) != 0

    def _strip_receivers(x: str):
        return x.strip()

    receivers = list(filter(_remove_empty_receivers, map(_strip_receivers, receivers)))
    print(receivers)
    receivers_as_text = MAILING_RECEIVERS_SEPARATOR.join(receivers)
    return mailing_list_repository.create_mailing_list(alias, receivers_as_text)


def get_mailing_list_by_alias(alias: str) -> MailingList:
    return mailing_list_repository.get_mailing_list_by_alias(alias)
