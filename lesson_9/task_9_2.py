class Road:

    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def asphalt_mass(self):
        value = (self._width * self._lenght * 25 * 5) // 1000
        return print(f'{self._lenght}м * {self._width}м * 25кг * 5см = {value}т.')


calculation = Road(20, 5000)
calculation.asphalt_mass()

