#!/usr/bin/env python3
import sys


def ft_command_quest(args: list | None = None) -> None:
    argc = len(sys.argv)
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if argc == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argc - 1}")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"Argument {i}: {arg}")
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    ft_command_quest()
