def insert0(x, ss):
    if ss != []:
        if x <= ss[0]:
            return [x] + ss
        else:
            return ss[0] + insert0(x, ss[1:])
    else:
        return [x]

def insert1(x, ss):
    def loop(ss, left):
        if ss != []:
            if x <= ss[0]:
                return left + [x] + ss
            else:
                return loop(ss[1:], left + [ss[0]])
        else:
            return [x]
    return loop(ss, [])

def insert(x, ss):
    left = []
    while ss != []:
        if x <= ss[0]:
            return left + [x] + ss
        else:
            ss, left = ss[1:], left + [ss[0]]
    return left + [x] + ss

def isort0(s):
    if s != []:
        return insert(s[0], isort0(s[1:]))
    else:
        return []

def isort1(s):
    def loop(s, ss):
        if s != []:
            return loop(s[1:], insert(s[0], ss))
        else:
            return ss
    return loop(s, [])

def isort(s):
    ss = []
    while s != []:
        s, ss = s[1:], insert(s[0], ss)
    return s + ss

def isort_for_version(s):
    ss = []
    for x in s:
        ss = insert(x, ss)
    return ss

# print(insert0(1, [2, 4, 5, 7, 8]))
# print(insert1(9, []))
# print(insert(6, [2, 4, 5, 7, 8]))
# print(isort0([3, 5, 4, 2]))
# print(isort1([6, 2, 4, 7, 8, 5]))
# print(isort([8, 0, 5, 7, 9, 4, 2, 1]))
# print(isort_for_version([6, 2, 4, 7, 8, 5]))
