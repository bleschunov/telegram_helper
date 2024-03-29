import load_dotenv
from telegram_helper.telethon_client import telethon_client


async def main():
    print(await telethon_client.get_me())

if __name__ == "__main__":
    with telethon_client:
        telethon_client.loop.run_until_complete(main())
