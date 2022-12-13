import time
import random

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

random_color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET])


def trasnsform_title():
    word = input('Write a title: ').replace(' ', '_').lower()
    num = input('Write the num: ')
    final_word = num + '_' + word + '.py'
    time.sleep(0.1)
    print(f'\n{random_color}{final_word}\n')

if __name__ == '__main__':
    trasnsform_title()