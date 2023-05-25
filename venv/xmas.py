def print_triangle(n):
    for size in range(1, n+1,2): #repeats
        print(("*"*size).center(n))

for i in range(3,8+1, 2):
    print_triangle(i)
