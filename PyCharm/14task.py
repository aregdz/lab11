#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    n = input("Введите значение: ")

    return n


def test_input(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def str_to_int(n):
    s = int(n)
    return s


def print_int(s):
    print(s)


if __name__ == '__main__':
    n = get_input()

    if test_input(n):
        s = str_to_int(n)
        print_int(s)
    else:
        print("Введенное значение не является числом!!!")