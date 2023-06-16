from abc import ABC

from repository.repository import Repository


class Shape(ABC, Repository):
    def get_all_x(self):
        """
        Получить массив координат x для всех вершин всех сущностей
        """
        return sum([entity.get_x() for entity in self.entities], [])

    def get_all_y(self):
        """
        Получить массив координат y для всех вершин всех сущностей
        """
        return sum([entity.get_y() for entity in self.entities], [])

    def get_all_label(self):
        """
        Получить массив координат label для всех вершин всех сущностей
        """
        return sum([entity.get_label() for entity in self.entities], [])
