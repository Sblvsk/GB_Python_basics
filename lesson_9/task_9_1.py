from time import sleep

class TrafficLight:

    __color = ["красный", "желтый", "зеленый"]
    time_sleeps = [7, 2, 5]

    def start(self):
        for time, color in enumerate(self.__color):
            sleep(self.time_sleeps[time])
            print(color)


a = TrafficLight()
a.start()

