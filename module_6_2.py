class Vehicle:

    __COLOR_VARIANTS  = ['red', 'blue', 'black']

    def __init__(self, owner:str, model: str, engine_power: int, color: str):
        self.new_color = None
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f"Модель:{self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя:{self.__engine_power}"

    def get_color(self):
        return f"Цвет:{self.__color}"

    def print_info(self):
        print(f"{self.get_model()}, {self.get_horsepower()}, {self.get_color()}, Владелец:{self.owner}")

    def set_color(self, new_color: str):
        if new_color.lower() in (color.lower() for color in self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        super().__init__(owner, model, engine_power, color)

vehicle = Vehicle("IVAN", "TOYOTA", "130", "red")
vehicle.print_info()
