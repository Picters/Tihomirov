import time
from colorama import Fore, init
import sys
import os
from art import *

ass = False

init()

clear()
print(text2art("Tihomirov"))
print("Для начала давайте ознакомимся с правилами игры.")
print("1. Тут не будет детского порно")
print("2. Цвет ваших мыслей выделяется " + Fore.CYAN + "ЭТИМ" + Fore.RESET + " цветом.")
print("3. Обязательно нажмите F11 или будет плохо (Пожайлуста)")
print("4. Не указывайте слишком большое имя пожайлуста, это может повлиять на отображение.")
print("5. " + Fore.RED + "Нельзя выбирать несуществующие варианты." + Fore.RESET)
print()
print(Fore.YELLOW + "Вы ознакомлены?" + Fore.RESET)
rules = input("(y/n): ")
if rules == "y":
    print(Fore.GREEN + "Спасибо)" + Fore.RESET)
    time.sleep(0.5)
    os.system("cls")
elif rules == "n":
    clear()
    print(Fore.RED + "Ну и иди нахуй тогда" + Fore.RESET)
    time.sleep(0.5)
    sys.exit()
else:
    clear()
    print(Fore.RED + "Ты даун?" + Fore.RESET)
    time.sleep(0.5)
    sys.exit()

name = input("Введите свое имя: ")
if sorted(name.lower()) == sorted("Tihomirov".lower()) or sorted(name.lower()) == sorted("тихомиров".lower()):
    print(Fore.RED + "Тихомиров уже есть." + Fore.RESET)
    time.sleep(0.5)
    sys.exit()

print(Fore.GREEN + "карина шлюха" + Fore.RESET)
time.sleep(1)
clear()

def slowprint(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear():
    os.system("cls")

def rule5():
    clear()
    print("5. " + Fore.RED + "Нельзя выбирать несуществующие варианты." + Fore.RESET)
    time.sleep(2)
    sys.exit()

def start():
    slowprint(f"""Тебя зовут {name}, ты учишься в 7А классе в школе №7. После первого прихода в школу ты запал на Матюнину Василису и спустя несколько дней полюбил ее. 
Ты не знаешь есть ли у нее парень или нет, но тебя будто это совсем не волновало. """, delay=0.05)
    input(Fore.YELLOW + "[ENTER]: " + Fore.RESET)
    clear()
    time.sleep(2)
    print("Время: 7:48")
    print("День недели: Понедельник")
    slowprint(Fore.CYAN + "Это мой первый учебный день. Нужно собраться, красиво одеться и пойти в школу." + Fore.RESET)
    print()
    print("1. Подготовится и пойти в школу")
    print(Fore.RED + "2. Выйти в окно" + Fore.RESET)
    choice = int(input(": "))
    if choice == 1:
        schoolday1()
    elif choice == 2:
        clear()
        time.sleep(3)
        slowprint(Fore.RED + "Ты долбаёб?" + Fore.RESET)
        time.sleep(0.5)
        sys.exit()
    else: rule5()

def schoolday1():
    clear()
    slowprint(Fore.CYAN + "Так вроде бы этот кабинет..." + Fore.RESET)
    time.sleep(1)
    slowprint("Василиса тоже подошла к кабинету и увидела тебя")
    time.sleep(1)
    slowprint(Fore.MAGENTA + f"{name} ПОСТОЙ!!!" + Fore.RESET)
    time.sleep(1)
    slowprint("Ты обернулся и в твоих глазах засияла она...")
    print()
    print("1. Спросить есть ли у нее парень ")
    print(Fore.RED + "2. Лапнуть за попу" + Fore.RESET)
    choice = int(input(": "))
    if choice == 1:
        slowprint(Fore.BLUE + "Слушай.. Василис.. А у тебя есть парень?" + Fore.RESET)
        time.sleep(0.5)
        slowprint(Fore.MAGENTA + "Ну конечно есть! А что?" + Fore.RESET)
        time.sleep(0.5)
        slowprint(Fore.BLUE + "Да так.. Ничего." + Fore.RESET)
        time.sleep(0.5)
        slowprint(Fore.MAGENTA + f"Ну ладно! Пока {name}!" + Fore.RESET)
        time.sleep(0.5)
        slowprint(Fore.CYAN + "ЭХ СУКА НУ ПОЧЕМУ ТАК...")
        time.sleep(0.5)
        cabinet1()
    elif choice == 2:
        ass = True
        slowprint("Ты тронул василисину задницу рукой")
        time.sleep(1)
        slowprint(Fore.MAGENTA + "Оу.. Сделаю вид что ничего не было)" + Fore.RESET)
        time.sleep(1)
        slowprint("Ты увидел как тихомиров наблюдал за вами из кабинета. Он ушел.")
        slowprint(Fore.CYAN + "БЛЯ ПИЗДА МНЕ" + Fore.RESET)
        time.sleep(1)
        slowprint(Fore.BLUE + "Слушай.. Василис.. А у тебя есть парень?" + Fore.RESET)
        time.sleep(0.5)
        slowprint(Fore.MAGENTA + "Ну конечно есть! А что?" + Fore.RESET)
        time.sleep(0.5)
        slowprint(Fore.BLUE + "Да так.. Ничего." + Fore.RESET)
        time.sleep(0.5)
        slowprint(Fore.MAGENTA + f"Ну ладно! Пока {name}!" + Fore.RESET)
        time.sleep(0.5)
        slowprint(Fore.CYAN + "ЭХ СУКА НУ ПОЧЕМУ ТАК...")
        time.sleep(0.5)
        cabinet1()

def cabinet1():
    sys.exit()


start()
