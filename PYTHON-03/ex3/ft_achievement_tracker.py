#!/usr/bin/env python3
import random


def gen_player_achievements(all_achievements: list[str]) -> set[str]:
    count = random.randint(4, len(all_achievements))
    return set(random.sample(all_achievements, count))


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    achievements = [
        "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
        "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
        "First Steps", "Collector Supreme", "Untouchable",
        "Sharp Mind", "Boss Slayer", "Hidden Path Finder"
    ]

    players = {
        "Alice": gen_player_achievements(achievements),
        "Bob": gen_player_achievements(achievements),
        "Charlie": gen_player_achievements(achievements),
        "Dylan": gen_player_achievements(achievements),
    }

    # Mostrar jugadores
    for name in players:
        ach = players[name]
        print(f"Player {name}: {ach}")

    # Todos los logros
    all_ach: set[str] = set()
    for name in players:
        ach = players[name]
        all_ach = all_ach.union(ach)
    print()
    print(f"All distinct achievements: {all_ach}\n")

    # Logros comunes
    common = None
    for name in players:
        ach = players[name]
        if common is None:
            common = ach
        else:
            common = common.intersection(ach)

    print(f"Common achievements: {common}\n")

    # Logros únicos por jugador
    for name in players:
        others: set[str] = set()
        for other_name in players:
            if other_name != name:
                others = others.union(players[other_name])

        unique = players[name].difference(others)
        print(f"Only {name} has: {unique}")
    print()
    # Logros faltantes
    for name in players:
        ach = players[name]
        missing = set(achievements).difference(ach)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
