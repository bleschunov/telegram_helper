import peewee as pw

import unittest
from unittest.mock import patch, Mock

from test import add_src_to_pythonpath

from telegram_helper.schema.mailing_list_schema import MailingList
from telegram_helper.repository import mailing_list_repository


class TestMailingListRepository(unittest.TestCase):
    @patch.object(MailingList, "get", side_effect=pw.DoesNotExist)
    def test_get_mailing_list_by_alias(self, MockMailingList: Mock):
        with self.assertRaises(ValueError):
            mailing_list_repository.get_mailing_list_by_alias(Mock())
            MockMailingList.get.assert_called_once()

    @patch.object(MailingList, "create", side_effect=pw.IntegrityError)
    def test_create_mailing_list(self, MockMailingList: Mock):
        with self.assertRaises(ValueError):
            mailing_list_repository.create_mailing_list(Mock(), Mock())
            MockMailingList.create.assert_called_once()


if __name__ == "__main__":
    unittest.main()
