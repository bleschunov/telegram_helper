import asyncio
from pathlib import Path
from typing import Optional, Annotated

import typer
from telethon.errors import ApiIdInvalidError
from rich import print

from telegram_helper.model import message_model, telegram_account_model, mailing_list_model
from telegram_helper.init_db import init_db as init_db_
from telegram_helper.printer import print_success, print_error

app = typer.Typer(pretty_exceptions_enable=False)


@app.command()
def add_telegram_account(alias: str, api_id: int, api_hash: str):
    try:
        telegram_account_db = telegram_account_model.add_telegram_account(alias, api_id, api_hash)
        print(telegram_account_db)
    except ApiIdInvalidError as e:
        print_error(str(e))


@app.command()
def init_db():
    init_db_()


@app.command()
def get_telegram_accounts(alias: Annotated[Optional[str], typer.Argument()] = None):
    try:
        if not alias:
            telegram_account_db_list = telegram_account_model.get_all_telegram_accounts()
            for account in telegram_account_db_list:
                print("•", account)
        else:
            print(telegram_account_model.get_telegram_account_by_alias(alias))
    except ValueError as e:
        print(e)


@app.command()
def send_message(telegram_account_alias: str, receiver: str, message_text: str):
    async def _send_message():
        try:
            await message_model.send_message(telegram_account_alias, receiver, message_text)
            print_success("Message was sent successfully!")
        except ValueError as e:
            print_error(str(e))

    asyncio.run(_send_message())


@app.command()
def create_mailing_list(alias: str, filename: str):
    mailing_list_path = Path.cwd() / "data" / "mailing_list" / filename
    receivers = mailing_list_model.extract_receivers_from_file(mailing_list_path)
    mailing_list_db = mailing_list_model.create_mailing_list(alias, receivers)
    print(mailing_list_db)


@app.command()
def send_messages_to_mailing_list(telegram_account_alias: str, mailing_list_alias: str, message_text: str):
    async def _send_messages_to_mailing_list():
        async for send_message_coroutine in message_model.send_messages_to_mailing_list_generator(
            telegram_account_alias,
            mailing_list_alias,
            message_text
        ):
            try:
                message = await send_message_coroutine
                print_success(f"Message was successfully sent to {message.peer_id}!")
            except ValueError as e:
                print_error(str(e))

    asyncio.run(_send_messages_to_mailing_list())


if __name__ == "__main__":
    app()
