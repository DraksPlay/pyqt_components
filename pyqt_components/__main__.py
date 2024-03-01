import argparse

from . import (
    commands
)


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    parser.add_argument("-n", "--name", default="app")

    args = parser.parse_args()

    if args.command == "init":
        commands.init(args.name)
    else:
        raise "Command not found"


if __name__ == "__main__":
    run()
