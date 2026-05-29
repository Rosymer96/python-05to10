from typing import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        first = spell1(target, power)
        second = spell2(target, power)
        return (first, second)
    return combined_spell


def power_amplifier(
        base_spell: Callable[[str, int], str],
        multiplier: int
) -> Callable[[str, int], str]:
    def amplified_power(target: str, power: int) -> str:
        new_power = power * multiplier
        new_spell = base_spell(target, new_power)
        return new_spell
    return amplified_power


def conditional_caster(
        condition: Callable[[str, int], bool],
        spell: Callable[[str, int], str],
) -> Callable[[str, int], str]:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return caster


def spell_sequence(
        spells: list[Callable[[str, int], str]]
) -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int) -> list[str]:
        results = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return sequence


def is_enough_energy(target: str, power: int) -> bool:
    return target == "Dragon" and power >= 10


def main() -> None:
    print("\nTesting spell combiner...")
    combiner = spell_combiner(fireball, heal)
    ex_combiner = combiner("Dragon", 10)
    print("Combined spell result:", end=" ")
    print(", ".join([x for x in ex_combiner]))

    print("\nTesting power amplifier...")
    amplified = power_amplifier(fireball, 3)
    ex_amplified = amplified("Goblin", 10)
    print(ex_amplified)

    print("\nTesting conditional caster...")
    castered = conditional_caster(is_enough_energy, fireball)
    print(castered("Dragon", 20))
    print(castered("Dragon", 8))

    print("\nTesting spellsequence...")
    sequence = spell_sequence([heal, fireball, heal])
    print("\n".join(sequence("Dinosar", 16)))


if __name__ == "__main__":
    main()
