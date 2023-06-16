from model.shape import Shape


class Circle(Shape):
    def __init__(self, center, radius):
        """
        Создание новой окружности с центром и радиусом
        :param center: центр круга - Point
        :param radius: радиус круга
        """
        self.center = center
        self.radius = float(radius)

    def get_x(self):
        return [self.center.x]

    def get_y(self):
        return [self.center.y]

    def get_label(self):
        return [self.center.label]
