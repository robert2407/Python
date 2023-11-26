class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def get_description(self):
        return f"{self.name} lives in {self.habitat}"

class Mammal(Animal):
    def __init__(self, name, habitat, fur_color):
        super().__init__(name, habitat)
        self.fur_color = fur_color

    def describe_mammal(self):
        description = self.get_description()
        return f"{description}, has {self.fur_color} fur"

class Bird(Animal):
    def __init__(self, name, habitat, wingspan, beak_color):
        super().__init__(name, habitat)
        self.wingspan = wingspan
        self.beak_color = beak_color

    def describe_bird(self):
        description = self.get_description()
        return f"{description}, wingspan: {self.wingspan} centimeters, beak color: {self.beak_color}"


class Fish(Animal):
    def __init__(self, name, habitat, scales_color):
        super().__init__(name, habitat)
        self.scales_color = scales_color

    def describe_fish(self):
        description = self.get_description()
        return f"{description}, scales color: {self.scales_color}"

if __name__ == "__main__":
    lion = Mammal("Lion", "Grasslands", "golden")
    puffin = Bird("Puffin", "Coastal areas", 30, "orange")
    shark = Fish("Shark", "Oceans", "gray")

    print(lion.describe_mammal())
    print(puffin.describe_bird())
    print(shark.describe_fish())
