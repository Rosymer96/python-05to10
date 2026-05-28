from typing import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        first = spell1(target, power)
        second = spell2(target, power)
        return [first, second]
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_power(target: str, power: int) -> Callable:
        new_power = power * multiplier
        new_spell = base_spell(target, new_power)
        return new_spell
    return amplified_power


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int):
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return caster

def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(spells: list[Callable]) -> list[Callable]:



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

    def is_enough_energy(target: str, power: int) -> bool:
        if target:
            return power >= 10

    castered = conditional_caster(is_enough_energy, fireball)
    print(castered("Dragon", 20))
    print(castered("Dragon", 8))







if __name__ == "__main__":
    main()
