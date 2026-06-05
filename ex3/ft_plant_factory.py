class Plant:
    def __init__(self, name: str, height: float, day: int) -> None:
        self.name = name
        self.height = height
        self.day = day

    def show(self) -> str:
        return (f"{self.name}: {round(self.height, 1)}cm, "
                f"{self.day} days old")


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    print(f"Created: {Plant('Rose', 25.0, 30).show()}")
    print(f"Created: {Plant('Oak', 200.0, 365).show()}")
    print(f"Created: {Plant('Tulip', 15.0, 20).show()}")
    print(f"Created: {Plant('Cactus', 10.0, 100).show()}")
    print(f"Created: {Plant('Sunflower', 80.0, 45).show()}")


if __name__ == "__main__":
    ft_plant_factory()
