from functools import wraps
import time
from typing import Callable, Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if "power" in kwargs:
                power = kwargs["power"]
            else:
                power = args[-1]
            if power < min_power:
                return ("Insufficient power for this spell")
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    attempts += 1
                    if attempts < max_attempts:
                        print(f"Spell failed, retrying... "
                              f"(attempt {attempts}/{max_attempts})")
            return (f"Spell casting failed after {max_attempts} attempts")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (len(name) >= 3
                and all(c.isalpha() or c.isspace() for c in name))

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball casted!"
    print("Result:", fireball())

    print("\nTesting power validator...")

    @power_validator(50)
    def cast_spell(power: int) -> str:
        return "Fireball!"
    print("Valid power:", cast_spell(power=60))
    print("Invalid power:", cast_spell(power=30))

    print("\nTesting retrying spell...")

    @retry_spell(3)
    def test_spell() -> None:
        attempts = 0
        if attempts < 2:
            attempts += 1
            raise Exception("Spell failed")
        print("Waaaaaaagh spelled !")
    print(test_spell())

    @retry_spell(3)
    def test_spell_arg(power: int) -> None:
        if power < 50:
            raise ValueError("Not enough power")
        print("Waaaaaaagh spelled !")
    test_spell_arg(power=60)

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Pepito Perez"))
    print(guild.validate_mage_name("Pepit0"))
    print(guild.cast_spell("Fireball", power=10))
    print(guild.cast_spell("Fireball", power=9))


if __name__ == "__main__":
    main()
