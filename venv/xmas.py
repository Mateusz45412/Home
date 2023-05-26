def print_triangle(n, total):
    for size in range(1, n+1,2): #repeats
        print(("*"*size).center(total))

def s(size):
    for i in range(3,size+1, 2):
        print_triangle(i, size)

s(8)