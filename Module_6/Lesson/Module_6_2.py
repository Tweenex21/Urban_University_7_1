class Vehicle:
    __COLOR_VARIANTS = ["красный", "синий", "зеленый", "черный", "белый"]

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    def __init__(self, owner, model, engine_power, color, trunk_size):
        super().__init__(owner, model, engine_power, color)
        self.trunk_size = trunk_size

    def get_trunk_size(self):
        return f"Размер багажника: {self.trunk_size} литров"

    def print_info(self):
        super().print_info()
        print(self.get_trunk_size())

# COLOR_VARIANTS = ["красный", "синий", "зеленый", "черный", "белый"]
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, "синий", 300)
vehicle1.print_info()
vehicle1.set_color("Фиолетовый")
vehicle1.set_color("Черный")
vehicle1.owner = "Vasyok"
vehicle1.print_info()