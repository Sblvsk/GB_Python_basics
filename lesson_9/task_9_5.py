
class Stationery:
    title = 'parent'
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Ручка")

class Pencil(Stationery):
    def draw(self):
        print("Карандаш")

class Handle(Stationery):
    def draw(self):
        print("Маркер")

a,b,c,d = Stationery(), Pen(), Pencil(),Handle()
a.draw()
b.draw()
c.draw()
d.draw()

