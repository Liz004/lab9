import random
from random import randint


def proc1():
    my_list = [randint(1, 10) for i in range(randint(2, 12))]
    name = int(input("Угадайте число из списка: "))
    print(*my_list)
    print(name)
    if user_num in my_list:
        print("Поздравляю!!!Вы угадали число")
    else:
        print("Такого числа нет!!!")


def proc2():
    my_list = [randint(1, 10) for i in range(randint(1, 10))]
    l = set(my_list)
    print(*my_list)
    for i in l:
        a = my_list.count(i)
        if a > 1:
            print(i, "встречается", a, "раз(a)")
    if len(my_list) == len(l):
        print("повторяющихся элементов в списке нет")


def proc3():
    week = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")
    num = int(input("сколько  вы хотите выходных: "))
    print("Рабочие", *week[:-num])
    print("Выходные", *week[-num:])


def proc4():
    from random import sample
    my_gruppa = ["Петров", "Сидоров", "Мочалина", "Кузьмин", "Порталенко"]
    gruppa2 = ["Андерсон", "Порталенко", "Иванов", "Дружинин", "Радин"]
    sport = tuple(random.sample(my_gruppa, 3) + random.sample(gruppa2, 3))
    print("Моя группа: ", *my_gruppa)
    print("другая группа: ", *gruppa2)
    print(*sport, len(sport))
    if "Иванов" in sport:
        print("Фамилия Иванов входит в список секции столько раз:", sport.count("Иванов"))
    else:
        print("Иванова нет  в секции")

