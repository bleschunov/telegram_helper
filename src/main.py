from telethon import TelegramClient

import load_dotenv
from telegram_helper.telegram_integration import send_telegram_message
from telegram_helper.telethon_client import telethon_client


async def main(client: TelegramClient):
    print(await send_telegram_message(client, "dmitrybleschunov", "Hello world!"))

if __name__ == "__main__":
    with telethon_client as c:
        telethon_client.loop.run_until_complete(main(c))
