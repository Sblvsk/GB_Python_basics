
class Car:
    def __init__(self, speed, color, name, is_polise):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_polise  #bool(is_polise)

    def go_car(self):
        print('Машина поехала')

    def stop_car(self):
        print("Машина остановалиась")

    def turn(self, direction):
        directions = ["налево", "направо", "назад"]
        self.direction = direction.lower()
        if self.direction.lower() in directions:
            print(f'Машина повернула {self.direction}')

    def speed_now(self):
        print(f"Текущая скорость {self.speed}")

class TownCar(Car):
    def __init__(self, speed, color, name, is_polise):
        super().__init__(speed, color, name, is_polise)

    def speed_now(self):
        if self.speed <= 60:
            print(f"Текущая скорость {self.speed}")
        else:
            print("Скорость превышена!!!")

class SportCar(Car):
    def __init__(self, speed, color, name, is_polise):
        super().__init__(speed, color, name, is_polise)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_polise):
        super().__init__(speed, color, name, is_polise)

    def speed_now(self):
        if self.speed <= 40:
            print(f"Текущая скорость {self.speed}")
        else:
            print("Скорость превышена!!!")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_polise):
        super().__init__(speed, color, name, is_polise)


bus = TownCar(61, "Красный", "Икарус", False)
bus.turn("Назад")
bus.speed_now()
bus.speed = 50
bus.speed_now()