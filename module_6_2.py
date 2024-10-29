class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, _engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = _engine_power
        self.__color = __color

    def get_model(self):
        return f"\033[34mМодель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model(),
        self.get_horsepower(),
        self.get_color(),
        self.owner, sep='\n'
              )

    def set_color(self, new_color):
        self.new_color = new_color
        if self.new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"\033[31mНельзя сменить цвет на {self.new_color}\033[0m")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
