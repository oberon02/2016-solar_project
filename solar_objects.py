# coding: utf-8
# license: GPLv3


class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    type = "star"
    """Признак объекта звезды"""

    def __init__(self, m, x, y, Vx, Vy, Fx, Fy, R, color):
        self.m = m
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.Fx = Fx
        self.Fy = Fy
        self.R = R
        self.color = color


    color = "red"
    """Цвет звезды"""

    image = None
    """Изображение звезды"""


class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    def __init__(self, m, x, y, Vx, Vy, Fx, Fy, R, color):
        self.m = m
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.Fx = Fx
        self.Fy = Fy
        self.R = R
        self.color = color

    image = None
    """Изображение планеты"""