from ex0 import AquaFactory, FlameFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2 import InvalidStrategyError, BattleStrategy


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    len_opp = len(opponents)
    try:
        print("*** Tournament ***")
        print(f"{len_opp} opponents involved")
        for i in range(len_opp):
            for j in range(i + 1, len_opp):
                factory_one, strategy_one = opponents[i]
                factory_two, strategy_two = opponents[j]

                creature_one = factory_one.create_base()
                creature_two = factory_two.create_base()
                print()
                print("* Battle *")

                print(creature_one.describe())
                print("vs.")
                print(creature_two.describe())
                print("now fight!")

                actions_one = strategy_one.act(creature_one)
                actions_two = strategy_two.act(creature_two)

                for action in actions_one:
                    print(action)

                for action in actions_two:
                    print(action)
    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    aqua_factory = AquaFactory()
    flame_factory = FlameFactory()
    healing_factory = HealingCreatureFactory()
    transforming_factory = TransformCreatureFactory()
    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    opponents_one = [
        (flame_factory, normal_strategy),
        (healing_factory, defensive_strategy)
        ]
    battle(opponents_one)
    print()
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    opponents_two = [
        (flame_factory, aggressive_strategy),
        (healing_factory, defensive_strategy)
    ]
    battle(opponents_two)
    print()
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    opponents_three = [
        (aqua_factory, normal_strategy),
        (healing_factory, defensive_strategy),
        (transforming_factory, aggressive_strategy)
    ]
    battle(opponents_three)


if __name__ == "__main__":
    main()
