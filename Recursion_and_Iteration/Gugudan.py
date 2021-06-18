def gugudan1():
    for i in range(2, 10):
        for j in range(2, 10):
            if j == 6:
                print("\n")
            print("{} x {} = {}".format(i, j, str(i * j).rjust(2)), end=' ')
        print("\n\n")

def gugudan2():
    for i in range(2, 10):
        for j in range(2, 6):
            print("{} x {} = {}".format(j, i, str(j * i).rjust(2)), end=' ')
        print("\n")
    print("\n")
    for i in range(2, 10):
        for j in range(6, 10):
            print("{} x {} = {}".format(j, i, str(j * i).rjust(2)), end=' ')
        print("\n")

# gugudan1()
gugudan2()
