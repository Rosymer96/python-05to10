#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int):
        self._name: str = name
        self._height: int = height

    def get_info(self) -> None:
        print(f"{self._name}: "
              f"{self._height}cm", end="")

    def grow(self, cms: int):
        self._height += cms


class FloweringPlant(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            color: str,
            ):
        super().__init__(name, height)
        self._color: str = color

    def get_info(self) -> None:
        super().get_info()
        print(f", {self._color} flowers (blooming)", end="")


class PrizeFlower(FloweringPlant):
    def __init__(
            self, name: str,
            height: int,
            color: str,
            prize: int,
            ):
        super().__init__(name, height, color)
        self._prize: int = prize

    def get_info(self) -> None:
        super().get_info()
        print(f", Prize points: {self._prize}", end="")


class GardenManager:
    _total_gardens: int = 0
    _all_instances: list["GardenManager"] = []

    def __init__(
            self,
            owner: str,
            plants: list[Plant]
            ):
        self._owner: str = owner
        self._plants = plants
        self._total_growth = 0
        self._total_plant = self.count_plants(plants)
        GardenManager._all_instances += [self]
        GardenManager._total_gardens += 1

    class GardenStats:
        def __init__(self, plants: list[Plant]):
            self._plants = plants
            self.regular = 0
            self.flowering = 0
            self.prize = 0

        def count_types(self):
            for plant in self._plants:
                type = plant.__class__.__name__
                if type == "PrizeFlower":
                    self.prize += 1
                elif type == "FloweringPlant":
                    self.flowering += 1
                else:
                    self.regular += 1

    def add_plant(self, plant: Plant) -> None:
        self._plants += [plant]
        self._total_plant += 1
        print(f"Added {plant._name} to {self._owner}'s garden")

    def grow_all(self, cms: int) -> None:
        print(f"{self._owner} is helping all plants grow...")
        for plant in self._plants:
            plant.grow(cms)
            print(f"{plant._name} grew {cms}cm")
            self._total_growth += cms
        print()

    def calculate_score(self) -> int:
        total = 0
        for plant in self._plants:
            total += plant._height
        return total

    @staticmethod
    def height_validation(plants: list[Plant]) -> bool:
        valid: bool = True
        for plant in plants:
            if plant._height < 0:
                valid = False
                break
        print(f"Height validation test: {valid}")
        return valid

    @staticmethod
    def count_plants(plants: list[Plant]) -> int:
        count = 0
        for plant in plants:
            count += 1
        return count

    @classmethod
    def create_garden_network(cls) -> None:
        print("Garden scores - ", end="")
        first = True
        for manager in cls._all_instances:
            if not first:
                print(", ", end="")
            print(f"{manager._owner}: {manager.calculate_score()}", end="")
            first = False
        print()

    @classmethod
    def get_total_managed(cls) -> int:
        print(f"Total gardens managed: {cls._total_gardens}")
        return cls._total_gardens

    def garden_report(self) -> None:
        print(f"=== {self._owner} Garden Report ===")
        print("Plants in garden:")
        for plant in self._plants:
            print("- ", end="")
            plant.get_info()
            print()
        print()
        print(f"Plants added: {self._total_plant}, Total growth: "
              f"{self._total_growth}cm")
        stats = GardenManager.GardenStats(self._plants)
        stats.count_types()
        print(f"Plant types: {stats.regular} regular, "
              f"{stats.flowering} flowering, "
              f"{stats.prize} prize flowers")
        print()


def main() -> None:
    print("=== Garden Management System Demo ===\n")
    alice = GardenManager("Alice", [])
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    print()
    alice.grow_all(1)
    alice.garden_report()
    alice.height_validation(alice._plants)
    bob = GardenManager("Bob", [rose])
    bob.calculate_score()
    GardenManager.create_garden_network()
    GardenManager.get_total_managed()


if __name__ == "__main__":
    main()
