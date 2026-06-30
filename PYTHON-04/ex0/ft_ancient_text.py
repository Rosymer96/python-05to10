#!/usr/bin/env python3
import sys
from typing import IO


def ft_read_text(f: IO[str]) -> None:
    content = f.read()
    print("---\n")
    print(f"{content}")
    print("\n---")


def main(args: list[str]) -> None:
    if len(args) != 2:
        print(f"Usage: {args[0]} <file>")
        return
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{args[1]}'")
        try:
            opened = open(args[1], 'r')
        except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
            print(f"Error opening file '{args[1]}': {e}")
            return
        ft_read_text(opened)
        opened.close()
        print(f"File '{args[1]}' closed.")


if __name__ == "__main__":
    main(sys.argv)
