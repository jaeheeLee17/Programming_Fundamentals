def mult1(m, n):
    if n > 0:
        return m + mult(m, n - 1)
    else:
        return 0

def mult2(m, n):
    def loop(n, ans):
        if n > 0:
            return loop(n - 1, ans + m)
        else:
            return ans
    return loop(n, 0)

def mult3(m, n):
    ans = 0
    while n > 0:
        n, ans = n - 1, ans + m
    return ans

def double(n):
    return n * 2

def halve(n):
    return n // 2

def fastmult1(m, n):
    if n > 0:
        if n % 2 == 0:
            return fastmult1(double(m), halve(n))
        else:
            return m + fastmult1(m, n - 1)
    else:
        return 0

def fastmult2(m, n):
    def loop(m, n, ans):
        if n > 0:
            if n % 2 == 0:
                return loop(double(m), halve(n), ans)
            else:
                return loop(m, n - 1, ans + m)
        else:
            return ans
    return loop(m, n, 0)

def fastmult3(m, n):
    ans = 0
    while n > 0:
        if n % 2 == 0:
            m, n, ans = double(m), halve(n), ans
        else:
            n, ans = n - 1, ans + m
    return ans

def Russian_mult1(m, n):
    def loop(m, n):
        if n > 1:
            if n % 2 == 0:
                return loop(double(m), halve(n))
            else:
                return m + loop(double(m), halve(n - 1))
        else:
            return m
    return loop(m, n)

def Russian_mult2(m, n):
    def loop(m, n, ans):
        if n > 1:
            if n % 2 == 0:
                return loop(double(m), halve(n), ans)
            else:
                return loop(double(m), halve(n - 1), ans + m)
        else:
            return m + ans
    return loop(m, n, 0)

def Russian_mult3(m, n):
    ans = 0
    while n > 1:
        if n % 2 == 0:
            m, n = double(m), halve(n)
        else:
            m, n, ans = double(m), halve(n - 1), ans + m
    return m + ans

# print(mult1(57, 86))
# print(mult2(57, 86))
# print(mult3(57, 86))
# print(fastmult1(57, 86))
# print(fastmult2(57, 86))
# print(fastmult3(57, 86))
# print(Russian_mult1(57, 86))
# print(Russian_mult2(57, 86))
# print(Russian_mult3(57, 86))
