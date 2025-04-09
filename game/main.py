import time
from colorama import Fore, init
import sys
import os
import pyfiglet

init()

os.system("cls")
print(pyfiglet.figlet_format("Tihomirov"))
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
    os.system("cls")
    print(Fore.RED + "Ну и иди нахуй тогда" + Fore.RESET)
    time.sleep(0.5)
    sys.exit()
else:
    os.system("cls")
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
os.system("cls")

def slowprint(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def rule5():
    os.system("cls")
    print("5. " + Fore.RED + "Нельзя выбирать несуществующие варианты." + Fore.RESET)
    time.sleep(2)
    sys.exit()

def start():
    slowprint(f"""Тебя зовут {name}, ты учишься в 7А классе в школе №7. После первого прихода в школу ты запал на Матюнину Василису и спустя несколько дней полюбил ее. 
Ты не знаешь есть ли у нее парень или нет, но тебя будто это совсем не волновало. """, delay=0.05)
    input(Fore.YELLOW + "[ENTER]: " + Fore.RESET)
    os.system("cls")
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
        os.system("cls")
        time.sleep(3)
        slowprint(Fore.RED + "Ты долбаёб?" + Fore.RESET)
        time.sleep(0.5)
        sys.exit()
    else: rule5()

def schoolday1():
    sys.exit()


start()