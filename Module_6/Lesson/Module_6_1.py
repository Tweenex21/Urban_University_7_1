class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} Съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} Не стал есть {food.name}")
            self.alive = False

class Predator(Mammal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


lion = Predator("Лев")
flower = Flower("Роза")
apple = Fruit("Яблоко")


lion.eat(apple)
print(f"Сытый Лев? {lion.fed}")
print(f"Живой Лев? {lion.alive}")


lion.eat(flower)
print(f"Сытый Лев? {lion.fed}")
print(f"Живой Лев? {lion.alive}")