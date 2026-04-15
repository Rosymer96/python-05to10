import sys
from typing import IO


def ft_read_text(f: IO) -> str:
    content = f.read()
    print(f"---\n\n{content}\n---")
    return content

def main(args: list) -> None:
    if len(args) == 1:
        print(f"Usage: {args[0]} <file>")
        return
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{args[1]}'")
        try:
            opened = open(args[1], 'r')
        except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
            print(f"Error opening file '{args[1]}': {e}")
            return
        content = ft_read_text(opened)
        lines = content.split('\n')
        for line in lines:
            line = line.append('#\n')
            print(line)
        opened.close()
        print(f"File '{args[1]}' closed.")


if __name__ == "__main__":
    main(sys.argv)
