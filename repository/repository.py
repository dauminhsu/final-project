class Repository:
    def __init__(self, entities=None):
        if entities is None:
            entities = []
        self.entities = entities

    def get(self):
        """
        Получить список сущностей
        :return: вернуть список сущностей в текущем репозитории
        """
        return self.entities

    def add(self, entity):
        """
        Добавить новую сущность в репозиторий
        :param entity: Добавлена сущность
        """
        if entity is not None:
            self.entities.append(entity)

    def clear(self):
        """
        Очистить все объекты в репозитории
        """
        self.entities.clear()
