import asyncio
from typing import Optional, Annotated

import typer
from telethon.errors import ApiIdInvalidError
from rich import print

from telegram_helper.model import message_model, telegram_account_model
from init_db import init_db as init_db_

app = typer.Typer(pretty_exceptions_enable=False)


@app.command()
def add_telegram_account(alias: str, api_id: int, api_hash: str):
    try:
        telegram_account_db = telegram_account_model.add_telegram_account(alias, api_id, api_hash)
        print(telegram_account_db)
    except ApiIdInvalidError as e:
        print(f"[bold red]{e}[/bold red]")


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
            print(f"[bold green]Message was sent successfully![/bold green]")
        except ValueError as e:
            print(e)

    asyncio.run(_send_message())


if __name__ == "__main__":
    app()
