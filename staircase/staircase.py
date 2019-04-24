def staircase(n):
    counter = n - 2
    for i in range(1, n):
        print(" " * counter, "#" * i)
        counter = counter - 1
    print("#" * n)

if __name__ == '__main__':
    staircase(6)
