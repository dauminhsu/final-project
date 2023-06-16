from model.shape import Shape


class Point(Shape):
    def __init__(self, x, y, label=''):
        """
        Создание новой точки с координатой и меткой
        :param x: координата x точки
        :param y: координата y точки
        :param label: метка точки (по умолчанию: '')
        """
        self.x = float(x)
        self.y = float(y)
        self.label = label

    def to_tuple(self):
        """
        Преобразование точки в кортеж координат x и y
        :return: Кортеж координат x и y
        """
        return self.x, self.y

    def get_x(self):
        return [self.x]

    def get_y(self):
        return [self.y]

    def get_label(self):
        return [self.label]

    def __eq__(self, other):
        if self is None and other is None:
            return True
        if self is None or other is None:
            return False
        return self.x == other.x and self.y == other.y
