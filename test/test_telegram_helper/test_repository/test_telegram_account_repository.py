import peewee as pw

import unittest
from unittest.mock import patch, Mock

from test import add_src_to_pythonpath

from telegram_helper.repository import telegram_account_repository
from telegram_helper.schema.telegram_account_schema import TelegramAccount


class TestTelegramAccountRepository(unittest.TestCase):
    @patch.object(TelegramAccount, "get", side_effect=pw.DoesNotExist)
    def test_get_telegram_account_by_alias(self, MockTelegramAccount: Mock):
        with self.assertRaises(ValueError):
            telegram_account_repository.get_telegram_account_by_alias(Mock())
            MockTelegramAccount.get.assert_called_once()

    @patch.object(TelegramAccount, "create", side_effect=pw.IntegrityError)
    def test_add_telegram_account(self, MockTelegramAccount: Mock):
        with self.assertRaises(ValueError):
            telegram_account_repository.add_telegram_account(Mock(), Mock(), Mock())
            MockTelegramAccount.create.assert_called_once()


if __name__ == "__main__":
    unittest.main()
