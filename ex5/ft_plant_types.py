class Plant:
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

    def show(self) -> str:
        return (f"{self._name}: {round(self._height, 1)}cm, "
                f"{self._day} days old")

    def grow(self) -> None:
        self._height += 2

    def age(self) -> None:
        self._day += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, day: int, color: str) -> None:
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
        print("[asking the rose to bloom]")
        self._bloomed = True


class Tree(Plant):
    def __init__(self, name: str, height: float, day: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, day)
        self._trunk_diameter = trunk_diameter

    def show(self) -> str:
        info = super().show()
        return f"{info}\nTrunk diameter: {round(self._trunk_diameter, 1)}cm"

    def produce_shade(self) -> None:
        print(f"[asking the {self._name.lower()} to produce shade]")
        print(f"Tree {self._name} now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self._trunk_diameter, 1)}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, day: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, day)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self) -> str:
        info = super().show()
        return (f"{info}\nHarvest season: {self._harvest_season}\n"
                f"Nutritional value: {self._nutritional_value}")

    def grow(self) -> None:
        self._height += 2.1
        self._nutritional_value += 1

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    print(rose.show())
    rose.bloom()
    print(rose.show())
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    print(oak.show())
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    print(tomato.show())
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    print(tomato.show())


if __name__ == "__main__":
    main()
