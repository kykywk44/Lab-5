class circle():
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        print(f'Радиус круга: {self.radius}')
    def set_radius(self, new_radius):
        self.radius = new_radius

c = circle(10)

try:
    i = int(input('Введите радиус круга или нажмите enter, \nчтобы оставить радиус по умолчанию (по умолчанию 10). \n'))
    if i > 0:
        c.set_radius(i)
        c.get_radius()
    else:
        print(f'Значение {i} неверно. Установлено значение по умолчанию.')
        c.get_radius()
except ValueError:
    c.get_radius()