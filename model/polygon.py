from model.shape import Shape


class Polygon(Shape):
    def __init__(self, points):
        """
        Создание нового полигона со списком вершин
        :param points: список вершин полигона - массив Point
        """
        self.points = points

    def to_points_tuple(self):
        """
        Получение списка всех точек, преобразованных в кортеж
        :return: вернуть список всех точек, преобразованных в кортеж в полигоне
        """
        return [point.to_tuple() for point in self.points]

    def get_x(self):
        return [point.x for point in self.points]

    def get_y(self):
        return [point.y for point in self.points]

    def get_label(self):
        return [point.label for point in self.points]
