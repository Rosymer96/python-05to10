import sys
from typing import IO


def ft_read_text(f: IO) -> None:
    print(f"Accessing file '{f}'")
    content = f.read()
    print(f"---\n{content}\n---")
    f.close()


def main(args: list) -> None:
    print("=== Cyber Archives Recovery ===")
    opened = open(args[1], 'r')
    try:
        ft_read_text(opened)
    except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
        print(f"Error opening file '{args[1]}': {e}")
        return
    print(f"File '{args[1]}' closed.")


if __name__ == "__main__":
    main(sys.argv)
