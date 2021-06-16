def get_int(message):
    s = input(message)
    while not s.isdigit():
        s = input(message)
    return int(s)

def remove_sign(s):
    if s[0] == '+':
        s = s.partition("+")
    elif s[0] == '-':
        s = s.partition("-")
    return s[2]

def get_int_signed(message):
    s = input(message)
    while not (remove_sign(s).isdigit()):
        s = input(message)
    return int(s)

def isfloat(s):
    (m, _, n) = s.partition(".")
    return (m.isdigit() and (n.isdigit() or n == "")) or m == "" and n.isdigit()

def get_float(message):
    s = input(message)
    while not (s.isdigit() or isfloat(s)):
        s = input(message)
    return float(s)

def get_fixed_signed(message):
    s = input(message)
    while not (remove_sign(s).isdigit() or isfloat(remove_sign(s))):
        s = input(message)
    return float(s)

result = get_fixed_signed("Input Value: ")
print(result)
