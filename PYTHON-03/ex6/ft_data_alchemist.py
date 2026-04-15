#!/usr/bin/env python3
import random


def ft_data_alchemist() -> None:
    print("=== Game Data Alchemist ===")
    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john',
               'kevin', 'Liam']
    print(f"Initial list of players: {players}")
    all_cap_players = [p.capitalize() for p in players]
    print(f"New list with all names capitalized: {all_cap_players}")
    cap_players = [p for p in players if p == p.capitalize()]
    print(f"New list of capitalized names only: {cap_players}")
    score_dict = {p: random.randint(0, 1000) for p in all_cap_players}
    print(f"Score dict: {score_dict}")
    scores = [score_dict[player] for player in score_dict]
    score_average = round(sum(scores) / len(scores), 2)
    print(f"Score average is {score_average}")
    high_scores = {player: score_dict[player] for player in score_dict if
                   score_dict[player] > score_average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    ft_data_alchemist()
