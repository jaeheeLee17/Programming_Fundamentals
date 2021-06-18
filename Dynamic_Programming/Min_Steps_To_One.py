def minsteps0(n):
    if n > 1:
        r = 1 + minsteps0(n - 1)
        if n % 2 == 0:
            r = min(r, 1 + minsteps0(n // 2))
        if n % 3 == 0:
            r = min(r, 1 + minsteps0(n // 3))
        return r
    else:
        return 0

def minsteps1(n):
    memo = [0] * (n + 1)
    def loop(n):
        if n > 1:
            if memo[n] != 0:
                return memo[n]
            else:
                memo[n] = 1 + loop(n - 1)
                if n % 2 == 0:
                    memo[n] = min(memo[n], 1 + loop(n // 2))
                if n % 3 == 0:
                    memo[n] = min(memo[n], 1 + loop(n // 3))
                return memo[n]
        else:
            return 0
    return loop(n)

def minsteps(n):
    memo = [0] * (n + 1)
    for i in range(1, n + 1):
        if i > 1:
            if memo[i] != 0:
                return memo[i]
            else:
                memo[i] = 1 + memo[i - 1]
                if i % 2 == 0:
                    memo[i] = min(memo[i], 1 + memo[i // 2])
                if i % 3 == 0:
                    memo[i] = min(memo[i], 1 + memo[i // 3])
        else:
            memo[i] = 0
    return memo[n]

# print(minsteps(1000))
