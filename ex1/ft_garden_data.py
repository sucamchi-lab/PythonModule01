class Plant:
    def __init__(self, name: str, height: float, day: int) -> None:
        self.name = name
        self.height = height
        self.day = day

    def show(self) -> str:
        return f"{self.name}: {self.height}cm, {self.day} days old"


def main() -> None:
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(rose.show())
    print(sunflower.show())
    print(cactus.show())


if __name__ == "__main__":
    main()
