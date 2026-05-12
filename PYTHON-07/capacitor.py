from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main() -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    healing_factory = HealingCreatureFactory()
    healing_creature = healing_factory.create_base()
    print(healing_creature.describe())
    print(healing_creature.attack())
    print(healing_creature.heal())

    print(" evolved:")
    evolved_factory = HealingCreatureFactory()
    evolved_creature = evolved_factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.heal())

    print("\nTesting Creature with transform capability")
    print(" base:")
    transforming_factory = TransformCreatureFactory()
    transform_creature = transforming_factory.create_base()
    print(transform_creature.describe())
    print(transform_creature.attack())
    print(transform_creature.transform())
    print(transform_creature.attack())
    print(transform_creature.revert())

    print(" evolved:")
    transform_evolved = transforming_factory.create_evolved()
    print(transform_evolved.describe())
    print(transform_evolved.attack())
    print(transform_evolved.transform())
    print(transform_evolved.attack())
    print(transform_evolved.revert())


if __name__ == "__main__":
    main()
