#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def cylinder():

    def circle(r):
        return math.pi * r**2

    r = float(input("Введите радиус цилиндра: "))
    h = float(input("Введите высоту цилиндра: "))
    side_area = 2 * math.pi * r * h
    full_area = side_area + 2 * circle(r)

    choice = input("Хотите получить только площадь боковой поверхности цилиндра? (да/нет): ")
    if choice.lower() == "да":
        print(f"Площадь боковой поверхности цилиндра: {side_area}")
    else:
        print(f"Полная площадь цилиндра: {full_area}")

if __name__ == '__main__':
    cylinder()