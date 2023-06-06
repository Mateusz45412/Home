import colorama
from colorama import Fore

sign = input(Fore.LIGHTBLUE_EX + "Wprowadź dowolny znak: ")

def print_segment(n, total_width):
    for size in range(1, n+1, 2): # repeats
        print((Fore.LIGHTGREEN_EX + sign * size).center(total-total_width))

# def tree(size):
#     for i in range(3, size+1, 2):
#         print_triangle(i, size)
#
# s(7)
print_segment(20, 24)
