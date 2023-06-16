from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_x(self):
        """
        Получить массив координат x для всех вершин
        """
        pass

    @abstractmethod
    def get_y(self):
        """
        Получить массив координат y для всех вершин
        """
        pass

    @abstractmethod
    def get_label(self):
        """
        Получить массив координат label для всех вершин
        """
        pass
