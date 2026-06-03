class Plant:
    def __init__(self, name: str, height: int, day: int) -> None:
        self._name = name
        self._height = height
        if height < 0:
            print("Error: Height cannot be negative.")
            self._height = 0
        self._day = day
        if day < 0:
            print("Error: Age cannot be negative.")
            self._day = 0

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._day

    def set_height(self, height: int) -> None:
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
        return (f"{self._name}: {round(float(self._height), 1)}cm, "
                f"{self._day} days old")

    def grow(self) -> None:
        self._height += 2

    def age(self) -> None:
        self._day += 1


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print("Plant created: " + rose.show())
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    print("Attempting to set negative height...")
    rose.set_height(-5)
    print()
    print("Attempting to set negative age...")
    rose.set_age(-10)
    print("Current state: " + rose.show())


if __name__ == "__main__":
    ft_garden_security()
