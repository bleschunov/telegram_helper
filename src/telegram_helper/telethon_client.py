import os

from telethon import TelegramClient

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
telethon_client = TelegramClient('anon', api_id, api_hash)
