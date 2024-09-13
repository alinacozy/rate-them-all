import random
from functools import cmp_to_key


def compare(a: str, b: str):
    while (True):
        answer = input(f"Что вы выбираете?\n1. {a} или 2. {b}?\n")
        if answer == '1':
            return 1
        elif answer == '2':
            return -1
        print("Вы ввели неправильно. Введите 1 или 2.")


if __name__ == '__main__':

    with open("data.txt", encoding="UTF-8") as file:
        arr = list(map(lambda x: x.strip('\n'), file.readlines()))
    random.shuffle(arr)
    arr.sort(key=cmp_to_key(compare), reverse=True)

    print("Ваш отсортированный список:")
    for i, elem in enumerate(arr, start=1):
        print(f"{i}. {elem}")
