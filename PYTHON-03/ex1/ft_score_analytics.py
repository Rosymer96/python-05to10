#!/usr/bin/env python3
import sys


def ft_score_analytics(args: list[str]) -> None:
    print("=== Player Score Analytics ===")
    scores = []
    for arg in args[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if not scores:
        print(f"No scores provided. Usage: python3 {args[0]} "
              "<score1> <score2> ...")
        return
    len_scores = len(scores)
    total = sum(scores)
    max_score = max(scores)
    min_score = min(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {len_scores}")
    print(f"Total score: {total}")
    print(f"Average score: {total / len_scores}")
    print(f"High score: {max_score}")
    print(f"Low score: {min_score}")
    print(f"Score range: {max_score - min_score}")


if __name__ == "__main__":
    ft_score_analytics(sys.argv)
