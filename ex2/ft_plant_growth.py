class Plant:
    def __init__(self, name: str, height: int, day: int) -> None:
        self.name = name
        self.height = height
        self.day = day

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.day} days old")

    def grow(self) -> None:
        self.height += 2

    def age(self) -> None:
        self.day += 1


def ft_plant_growth() -> None:
    rose = Plant("Rose", 25, 30)
    initial_height = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for days in range(1, 7):
        print(f"=== Day {days} ===")
        rose.grow()
        rose.age()
        rose.show()
    growth = rose.height - initial_height
    print(f"Growth this week: {growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
