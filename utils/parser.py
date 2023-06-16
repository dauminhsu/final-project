import re

from model.point import Point


def parse_number(raw):
    """
    Разобрать число с плавающей запятой из строки
    :param raw: необработанная строка должна быть проанализирована
    :return: вернуть число с плавающей запятой, если его можно проанализировать, иначе вернуть None
    """
    try:
        return float(raw)
    except ValueError:
        return None


def parse_point(raw):
    """
    Разобрать точку (Point) из строки
    :param raw: необработанная строка должна быть проанализирована
    :return: вернуть точку (Point), если его можно проанализировать, иначе вернуть None
    """
    args = [arg.strip() for arg in re.split(r'[\s,()]+', raw) if arg.strip()]

    if len(args) != 3:
        return None
    if parse_number(args[1]) is None:
        return None
    if parse_number(args[2]) is None:
        return None

    return Point(args[1], args[2], args[0])
