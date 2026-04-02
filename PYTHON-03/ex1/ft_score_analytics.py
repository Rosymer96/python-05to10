#!/usr/bin/env python3
import sys


def ft_score_analytics(args: list | None = None) -> None:
    print("=== Player Score Analytics ===")
    scores = []
    if len(sys.argv)  > 0:
        for arg in sys.argv[1:]:
            try:
                scores.append(int(arg))
            except ValueError:
                print(f"Invalid parameter: {arg}")
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    ft_score_analytics()
