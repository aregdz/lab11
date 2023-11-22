#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def help1():
    """"
    Функция для вывода списка команд
    """
    # Вывести справку о работе с программой.
    print("Список команд:\n")
    print("add - добавить рейс;")
    print("list - вывести список рйсов;")
    print("select <тип> - вывод на экран пунктов назначения и номеров рейсов для данного типа самолёта")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def add1():
    """"
    Функция для добавления информации о новых рейсах
    """
    # Запросить данные о работнике.
    name = input("Название пункта назначения рейса? ")
    number = int(input("Номер рейса? "))
    tip = input("Тип самолета? ")
    # Создать словарь.
    i = {
        'name': name,
        'number': number,
        'tip': tip,
    }

    return i


def error1():
    """"
    функция для неопознанных команд
    """
    print(f"Неизвестная команда {command}")


def list(aircrafts):
    """"
    Функция для вывода списка добавленных рейсов
    """
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 8
    )
    print(line)

    # Вывести данные о всех сотрудниках.
    for idx, i in enumerate(aircrafts, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                idx,
                i.get('name', ''),
                i.get('number', ''),
                i.get('tip', '')
            )
        )
    print(line)


def select(command, aircrafts):
    """""
    Функция для получения номера рейса и пункта назначения по заднному типу самолёта.
    """
    # Разбить команду на части для выделения номера года.
    parts = input("Введите значение: ")
    # Проверить сведения работников из списка.
    count = 0

    for i in aircrafts:
        for k, v in i.items():

            if v == parts:
                print("Пункт назначения - ", i["name"])
                print("Номер рейса - ", i["number"])
                count += 1
    # Если счетчик равен 0, то работники не найдены.

    if count == 0:
        print("Рейс с заданным типом самолёта не найден.")


def main():
    """"
    Главная функция программы.
    """
    print("Список команд:\n")
    print("add - добавить рейс;")
    print("list - вывести список рйсов;")
    print("select <тип> - вывод на экран пунктов назначения и номеров рейсов для данного типа самолёта")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")
    # Список работников.
    aircrafts = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.

        match command:
            case 'exit':
                break

            case 'add':
                # Добавить словарь в список.
                i = add1()
                aircrafts.append(i)
                # Отсортировать список в случае необходимости.
                if len(aircrafts) > 1:
                    aircrafts.sort(key=lambda item: item.get('name', ''))

            case 'list':
                list(aircrafts)

            case 'select':
                select(command, aircrafts)

            case 'help':
                help1()

            case _:
                error1()


if __name__ == '__main__':
    main()
