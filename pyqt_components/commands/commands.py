import os
import pathlib

from .init import (
    app_text
)


def init(name: str):
    path = pathlib.Path().cwd()
    directory = path / name
    if not os.path.exists(str(directory)):
        os.mkdir(str(directory))
    else:
        raise "Directory exist"

    with open(str(directory / "app.py"), "w", encoding="utf-8") as file:
        file.write(app_text)

    os.mkdir(str(directory / "components"))






