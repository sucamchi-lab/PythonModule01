class Plant:
    class PlantStats:
        def __init__(self) -> None:
            self._grow = 0
            self._age = 0
            self._show = 0
            self._shade = 0

        def _increment_grow(self) -> None:
            self._grow += 1

        def _increment_age(self) -> None:
            self._age += 1

        def _increment_show(self) -> None:
            self._show += 1

        def _increment_shade(self) -> None:
            self._shade += 1

        def display(self, is_tree: bool = False) -> str:
            result = (f"Stats: {self._grow} grow, {self._age} age, "
                      f"{self._show} show")
            if is_tree:
                result += f"\n{self._shade} shade"
            return result

    def __init__(self, name: str, height: float, day: int) -> None:
        self._name = name
        self._height = height
        if height < 0:
            print("Error: Height cannot be negative.")
            self._height = 0.0
        self._day = day
        if day < 0:
            print("Error: Age cannot be negative.")
            self._day = 0
        self._stats = Plant.PlantStats()

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._day

    def set_height(self, height: float) -> None:
        if height < 0:
            print("Error: Height cannot be negative.")
            print("Height update rejected.")
            return
        self._height = height
        print(f"Height updated: {self._height}cm.")

    def set_age(self, day: int) -> None:
        if day < 0:
            print("Error: Age cannot be negative.")
            print("Age update rejected.")
            return
        self._day = day
        print(f"Age updated: {self._day} days.")

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> str:
        self._stats._increment_show()
        return (f"{self._name}: {round(self._height, 1)}cm, "
                f"{self._day} days old")

    def grow(self) -> None:
        self._height += 2
        self._stats._increment_grow()

    def age(self) -> None:
        self._day += 1
        self._stats._increment_age()


class Flower(Plant):
    def __init__(self, name: str, height: float, day: int,
                 color: str) -> None:
        super().__init__(name, height, day)
        self._color = color
        self._bloomed = False

    def show(self) -> str:
        info = super().show()
        if self._bloomed is True:
            bloom_status = "is blooming beautifully!"
        else:
            bloom_status = "has not bloomed yet"
        return (f"{info}\nColor: {self._color}\n"
                f"{self._name} {bloom_status}")

    def bloom(self) -> None:
        self._bloomed = True

    def grow(self) -> None:
        self._height += 8
        self._stats._increment_grow()


class Tree(Plant):
    def __init__(self, name: str, height: float, day: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, day)
        self._trunk_diameter = trunk_diameter

    def show(self) -> str:
        info = super().show()
        return (f"{info}\n"
                f"Trunk diameter: {round(self._trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self._name.lower()} to produce shade]")
        print(f"Tree {self._name} now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self._trunk_diameter, 1)}cm wide.")
        self._stats._increment_shade()


class Vegetable(Plant):
    def __init__(self, name: str, height: float, day: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, day)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self) -> str:
        info = super().show()
        return (f"{info}\n"
                f"Harvest season: {self._harvest_season}\n"
                f"Nutritional value: {self._nutritional_value}")

    def grow(self) -> None:
        self._height += 2.1
        self._nutritional_value += 1
        self._stats._increment_grow()

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1


class Seed(Flower):
    def __init__(self, name: str, height: float, day: int,
                 color: str) -> None:
        super().__init__(name, height, day, color)
        self._seeds = 0

    def show(self) -> str:
        info = super().show()
        return f"{info}\nSeeds: {self._seeds}"

    def bloom(self) -> None:
        self._bloomed = True
        self._seeds = 42

    def grow(self) -> None:
        self._height += 30
        self._stats._increment_grow()

    def age(self) -> None:
        self._day += 20
        self._stats._increment_age()


def display_plant_statistics(plant: Plant) -> None:
    name = plant._name
    print(f"[statistics for {name}]")
    is_tree = isinstance(plant, Tree)
    print(plant._stats.display(is_tree))


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> "
          f"{Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> "
          f"{Plant.is_older_than_a_year(400)}")
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    print(rose.show())
    display_plant_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    print(rose.show())
    display_plant_statistics(rose)
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    print(oak.show())
    display_plant_statistics(oak)
    oak.produce_shade()
    display_plant_statistics(oak)
    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    print(sunflower.show())
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    print(sunflower.show())
    display_plant_statistics(sunflower)
    print()
    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    print(anonymous.show())
    display_plant_statistics(anonymous)


if __name__ == "__main__":
    main()
