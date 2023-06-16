from model.shape import Shape


class Segment(Shape):
    def __init__(self, start, end):
        """
        Создание сегмента с 2 конечными точками
        :param start: первая конечная точка - Point
        :param end: вторая конечная точка - Point
        """
        self.start = start
        self.end = end

    def get_x(self):
        return [self.start.x, self.end.x]

    def get_y(self):
        return [self.start.x, self.end.x]

    def get_label(self):
        return [self.start.label, self.end.label]
