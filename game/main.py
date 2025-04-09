import time
from colorama import Fore, init
import sys
import os

init()
print("Пожайлуста нажмите F11)))")
name = input("Введите свое имя: ")
print("карина шлюха")
time.sleep(2)
os.system("cls")

def slowprint(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def part1():
    slowprint(f"Тебя зовут {name}, и ты учишься в 7А классе в школе №7. После первого прихода в школу ты запал на Матюнину Василису и спустя несколько дней полюбил ее. Ты не знаешь есть ли у нее парень или нет, но тебя будто это совсем не волновало. ", delay=0.05)
    input(Fore.YELLOW + "[ENTER]: " + Fore.RESET)


part1()