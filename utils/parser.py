import re

from model.point import Point


def parse_number(raw):
    try:
        return float(raw)
    except ValueError:
        return None


def parse_point(raw):
    args = [arg.strip() for arg in re.split(r'[\s,()]+', raw) if arg.strip()]

    if len(args) != 3:
        return None
    if parse_number(args[1]) is None:
        return None
    if parse_number(args[2]) is None:
        return None

    return Point(args[1], args[2], args[0])
