def gcd1(m, n):
    while n != 0:
        m, n = n, m % n
    return abs(m)

def gcd2(m, n):
    def loop(m, n, k):
        if not (m == 0 or n == 0):
            if m % 2 == 0 and n % 2 == 0:
                return loop(m // 2, n // 2, k * 2)
            elif m % 2 == 0 and n % 2 == 1:
                return loop(m // 2, n, k)
            elif m % 2 == 1 and n % 2 == 0:
                return loop(m, n // 2, k)
            elif m <= n:
                return loop(m, (n - m) // 2, k)
            else:
                return loop(n, (m - n) // 2, k)
        else:
            if m == 0:
                return abs(n * k)
            else:
                return abs(m * k)
    return loop(m, n, 1)

def gcd3(m, n):
    k = 1
    while not (m == 0 or n == 0):
        if m % 2 == 0 and n % 2 == 0:
            m, n, k = m // 2, n // 2, k * 2
        elif m % 2 == 0 and n % 2 == 1:
            m = m // 2
        elif m % 2 == 1 and n % 2 == 0:
            n = n // 2
        elif m <= n:
            n = n - m
        else:
            m, n = n, m - n
    if m == 0:
        return abs(n * k)
    else:
        return abs(m * k)

# print(gcd1(18, 48))
# print(gcd2(18, 48))
# print(gcd3(18, 48))
