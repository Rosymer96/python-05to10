#!/usr/bin/env python3
import sys


def ft_command_quest(args: list) -> None:
    argc = len(args)
    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")
    if argc == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argc - 1}")
        i = 1
        for arg in args[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    ft_command_quest(sys.argv)
