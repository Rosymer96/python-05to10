#!/usr/bin/env pyhton3
import sys
from typing import IO


def ft_read_text(f: IO[str]) -> str:
    content = f.read()
    print("---\n")
    print(f"{content}")
    print("\n---")
    return content


def main(args: list[str]) -> None:
    if len(args) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{args[1]}'")

    try:
        opened = open(args[1], 'r')
    except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
        sys.stderr.write(f"[STDERR] Error opening file '{args[1]}': {e}\n")
        return

    content = ft_read_text(opened)
    opened.close()
    print(f"File '{args[1]}' closed.")

    print("\nTransform data:")
    print("---\n")
    lines = content.split('\n')
    new_content = ""
    for line in lines:
        if line != "":
            new_content += line + "#\n"
    print(new_content)
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    file_name = sys.stdin.readline().strip()

    if file_name == "":
        print("Not saving data.")
    else:
        print(f"Saving data to '{file_name}'")
        try:
            new_file = open(file_name, 'w')
            new_file.write(new_content)
            new_file.close()
            print(f"Data saved in file '{file_name}'.")
        except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
            sys.stderr.write(f"[STDERR] Error opening file '{file_name}':"
                             f" {e}\n")
            print("Data not saved.")


if __name__ == "__main__":
    main(sys.argv)
