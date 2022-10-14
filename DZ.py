
import os
import math
from random import randint

def clear_screen():
    os.system('cls' if os == 'nt' else 'clear')

def random_int_fill_list(size, limfrom, limto):
    new_list = []
    for i in range(size):
        new_list.append(randint(limfrom, limto))
    return new_list

"""
22. Задайте список из нескольких чисел. Напишите программу, которая найдёт
сумму элементов списка, стоящих на нечётной позиции.
"""

def task_20():
    clear_screen()
    string_1 = ['sdf34sdf', 'lkj324o', 'poics99l', '93n1', 'mklja56a8']
    print(string_1)
    numb = int(input('Введите искомое число: '))
    count = 0
    for i in string_1:
        # if i.find(str(numb)) != -1:
        #     print(f'{i} содержит {numb}')
        if str(numb) in i:
            print(f'{i} содержит {numb}')
            count += 1
    if count == 0:
        print(f'{numb} не содержится в списке')


def task_20_1():
    clear_screen()
    str_1 = ['sdf34sdf', 'lkj324o', 'poics99l', '93n1', 'mklja56a8']
    print(str_1)
    while True:
        try:
            digit = int(input('Введите любое целое число: '))
        except Exception:
            clear_screen()
            print('Введите целое число!')
        else:
            break

    incl = list(filter(lambda x: x.count(str(digit)) > 0, str_1))
    if len(incl) == 0:
        print(f'Число {digit} нигде не содержится!')
    else:
        print(f'Число {digit} содержится в {incl}')
        
"""
22. Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.
"""

def task_22():
    clear_screen()
    size = 10
    rand_from = -44
    rand_to = 44
    my_list = random_int_fill_list(size, rand_from, rand_to)
    sum_of_odd_ind_elms = 0
    for i in range(1, len(my_list), 2):
        sum_of_odd_ind_elms += my_list[i]
    print(f'Сумма элементов списка {my_list} с нечетными индексами = {sum_of_odd_ind_elms}')


def task_22_1():
    clear_screen()
    my_list = [randint(-44, 44) for x in range(10)]
    new_list = list(filter(lambda x: my_list.index(x) % 2, my_list))
    print(new_list)
    sum_of_odd_ind_elms = sum(new_list)
    print(f'Сумма элементов списка {my_list} с нечетными индексами = {sum_of_odd_ind_elms}')
    
"""
23. Напишите программу, которая найдёт произведение пар чисел списка. Парой
    считаем первый и последний элемент, второй и предпоследний и т.д.
"""

def task_23(): 
    os.system('sls' if os == 'nt' else 'clear')
    size = int(input('Введите количество элементов списка: '))
    rand_from = 0
    rand_to = 20
    my_list = random_int_fill_list(size, rand_from, rand_to)
    pairs_mult = 1
    res = []
    for i in range(math.ceil(size / 2)):
        pairs_mult = my_list[i] * my_list[size - 1 - i]
        res.append(pairs_mult)
    print(
        f'Произведения пар элементов списка {my_list} "снаружи внутрь" = {res}')
    print()
    
def task_23_1():
    os.system('sls' if os == 'nt' else 'clear')
    size = int(input('Введите количество элементов списка: '))
    my_list = [randint(0, 20) for i in range(size)]
    new_list = [my_list[i] * my_list[-1 - i] for i in range(math.ceil(size / 2))]
    new_list = list(enumerate(new_list))
    print(f'Произведения пар элементов списка {my_list} "снаружи внутрь" = {new_list}')



# task_20()
# task_20_1()
# task_22()
task_22_1()
# task_23()
# task_23_1()


