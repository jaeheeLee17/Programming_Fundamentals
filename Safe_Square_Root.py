def isfloat(s):
    (m, _, n) = s.partition(".")
    return (m.isdigit() and (n.isdigit() or n == "")) or m == "" and n.isdigit()

def stop():
    cont = input('Would you like to continue? (y / n) ')
    while not (cont == 'y' or cont == 'n'):
        cont = input('Would you like to continue? (y / n) ')
    return cont == 'n'

def safe_sqrt():
    import math
    print("We will find the square root.")
    print("Please enter a number greater than or equal to 0.")
    while True:
        print("Enter the number: ")
        s = input()
        while not isfloat(s) or float(s) < 0:
            print("Enter the number: ")
            s = input()
        result = round(math.sqrt(float(s)), 4)
        print("The square root of {} is {}.".format(s, result))
        if stop():
            break
    print("GoodBye.")

safe_sqrt()
