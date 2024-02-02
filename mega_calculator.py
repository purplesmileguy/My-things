import os
import random
import pygame
import threading
import time
import pyfiglet
from colorama import Fore, Style, init

init(autoreset=True)

def play_background_music(music_files):
    pygame.init()
    pygame.mixer.init()

    def play_music():
        while True:
            music_file = random.choice(music_files)
            music_path = os.path.join('music1', music_file)
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play()
            print(" ")
            print(f"{Fore.CYAN}Играет:{Style.RESET_ALL} {music_file}\n")
            print(" ")
            while pygame.mixer.music.get_busy():
                time.sleep(1)

    music_thread = threading.Thread(target=play_music)
    music_thread.start()

def calculator():
    while True:
        try:
            # Получаем ввод от пользователя
            expression = input(f"{Fore.CYAN}Введите математическое выражение (для выхода введите 'clear'): {Style.RESET_ALL}")

            # Проверяем, нужно ли выйти
            if expression.lower() == 'clear':
                calculator()
            else:
                # Рассчитываем результат и выводим его
                result = eval(expression)
                print(f"{Fore.GREEN}Результат: {result}{Style.RESET_ALL}")

                # Сохраняем в текстовый файл
                with open('logs.txt', 'a') as file:
                    file.write(f"{expression} = {result}\n")

        except Exception as e:
            print(f"{Fore.RED}Ошибка: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    pygame.init()

    music1_files = [f for f in os.listdir('music1') if f.endswith('.mp3')]
    print(f"{Fore.YELLOW}Loading...{Style.RESET_ALL}")
    
    time.sleep(1)  # Задержка в 1 секунду
    os.system('cls')
    time.sleep(0.3)
    result = pyfiglet.figlet_format("PurpleCode")
    print(f"{Fore.CYAN}{result}{Style.RESET_ALL}")

    play_background_music(music1_files)
    time.sleep(0.1)
    calculator()

    pygame.quit()
