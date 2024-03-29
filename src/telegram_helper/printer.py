from rich import print


def _print_colorful(color: str, text: str):
    print(f"[{color}]{text}[/{color}]")


def print_success(text: str):
    _print_colorful("bold green", text)


def print_error(text: str):
    _print_colorful("bold red", text)
