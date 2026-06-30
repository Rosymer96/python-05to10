#!/usr/bin/env python3
class Plant:
    class Stats:
        def __init__(self) -> None:
            self.grow_counter: int = 0
            self.age_counter: int = 0
            self.show_counter: int = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_counter} grow, {self.age_counter} age, "
                  f"{self.show_counter} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self.set_height(height, False)
        self.set_age(age, False)
        self.stats = self.Stats()

    def show_stats(self) -> None:
        self.stats.display()

    def set_height(self, val: float, print_set: bool = True) -> None:
        if val < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = val
            if print_set:
                print(f"Height updated: {self._height}cm")

    def set_age(self, val: int, print_set: bool = True) -> None:
        if val < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = val
            if print_set:
                print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def grow(self, cm: float) -> None:
        self.set_height(self._height + cm, False)
        self.stats.grow_counter += 1

    def age(self, days: int) -> None:
        self.set_age(self._age + days, False)
        self.stats.age_counter += 1

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self._height:.1f}cm, {self._age}"
              f" days old")
        self.stats.show_counter += 1

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        if age > 365:
            res = True
        else:
            res = False
        print(f"Is {age} days more than a year? -> {res}")
        return res

    @classmethod
    def create_anonymous_plant(cls) -> 'Plant':
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(
            self,
            name: str,
            _height: float,
            _age: int,
            color: str,
            is_bloom: bool = False
            ) -> None:
        super().__init__(name, _height, _age)
        self.color: str = color
        self.is_bloom: bool = is_bloom

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_bloom is False:
            print(f" {self.name.capitalize()} has not bloomed yet")
        else:
            print(f" {self.name.capitalize()} is blooming beautifully!")

    def bloom(self, print_act: bool = True) -> None:
        if print_act:
            print(f"[asking the {self.name} to bloom]")
        self.is_bloom = True
        self.show()

    def grow_bloom(self, cm) -> None:
        print(f"[asking the {self.name} to grow and bloom]")
        self.grow(8)
        self.bloom(False)


class Seed(Flower):
    def __init__(
            self,
            name: str,
            _height: float,
            _age: int,
            color: str,
            is_bloom: bool = False,
            number_of_seed: int = 0
            ) -> None:
        super().__init__(name, _height, _age, color, is_bloom)
        self.number_of_seed = number_of_seed

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.number_of_seed}")

    def bloom(self, print_act: bool = True) -> None:
        self.number_of_seed += 42
        super().bloom(False)

    def grow_age_bloom(self, cm: float, days: int) -> None:
        print(f"[make {self.name} grow, age and bloom]")
        self.grow(cm)
        self.age(days)
        self.bloom()


class Tree(Plant):
    def __init__(
            self,
            name: str,
            _height: float,
            _age: int,
            trunk_diameter: float,
            ) -> None:
        super().__init__(name, _height, _age)
        self.trunk_diameter: float = trunk_diameter
        self.shade_counter = 0

    def show_stats(self) -> None:
        self.stats.display()
        print(f"{self.shade_counter} shade")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name.capitalize()} now produces a shade of "
              f"{self._height:.1f}cm long and {self.trunk_diameter:.1f}"
              f"cm wide.")
        self.shade_counter += 1

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            _height: float,
            _age: int,
            harvest_season: str,
            nutritional_value: int = 0
            ) -> None:
        super().__init__(name, _height, _age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def age(self, days: int) -> None:
        super().age(days)
        self.nutritional_value += days

    def grow(self, cm: float) -> None:
        super().grow(cm)

    def grow_and_age(self, cm: float, days: int) -> None:
        print(f"[make {self.name} grow and age for {days} days]")
        self.age(days)
        self.grow(cm)
        self.show()


def display_any_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name.capitalize()}]")
    plant.show_stats()


def main() -> None:
    print("=== Garden statistics ===")
    Plant.is_older_than_year(30)
    Plant.is_older_than_year(400)
    print()
    print("=== Flower")
    rose = Flower("rose", 15, 10, "red")
    rose.show()
    display_any_stats(rose)
    rose.grow_bloom(8)
    display_any_stats(rose)
    print()
    print("=== Tree")
    oak = Tree("oak", 200, 365, 5)
    oak.show()
    display_any_stats(oak)
    oak.produce_shade()
    display_any_stats(oak)
    print()
    print("=== Seed")
    sunflower = Seed("sunflower", 80, 45, "yellow")
    sunflower.show()
    sunflower.grow_age_bloom(30, 20)
    display_any_stats(sunflower)
    print()
    print("=== Anonymous")
    anonymous = Plant.create_anonymous_plant()
    anonymous.show()
    display_any_stats(anonymous)


if __name__ == "__main__":
    main()
