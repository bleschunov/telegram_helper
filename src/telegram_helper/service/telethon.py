from pathlib import Path

from telethon.sync import TelegramClient


def get_telegram_client(alias: str, api_id: int, api_hash: str) -> TelegramClient:
    session_folder_path = str(Path.cwd() / "data" / "telegram_session" / str(alias))
    return TelegramClient(session_folder_path, api_id, api_hash)
