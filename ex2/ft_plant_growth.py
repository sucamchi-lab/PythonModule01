class Plant:
    def __init__(self, name: str, height: float, day: int) -> None:
        self.name = name
        self.height = height
        self.day = day

    def show(self) -> str:
        return f"{self.name}: " \
               f"{round(self.height, 1)}cm, {self.day} days old"

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.day += 1


def main() -> None:
    rose = Plant("Rose", 25.0, 30)
    initial_height = rose.height
    print("=== Garden Plant Growth ===")
    print(rose.show())
    for days in range(1, 8):
        print(f"=== Day {days} ===")
        rose.grow()
        rose.age()
        print(rose.show())
    growth = rose.height - initial_height
    print(f"Growth this week: {round(growth, 1)}cm")


if __name__ == "__main__":
    main()
