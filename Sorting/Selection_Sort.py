def ssort0(s):
    if s != []:
        smallest = min(s)
        s.remove(smallest)
        return [smallest] + ssort0(s)
    else:
        return []

def ssort1(s):
    def loop(s, ss):
        if s != []:
            smallest = min(s)
            s.remove(smallest)
            return loop(s, ss + [smallest])
        else:
            return ss
    return loop(s, [])

def ssort2(s):
    def loop(s, ss):
        if s != []:
            smallest = min(s)
            s.remove(smallest)
            ss.append(smallest)
            return loop(s, ss)
        else:
            return ss
    return loop(s, [])

def ssort3(s):
    ss = []
    while s != []:
        smallest = min(s)
        s.remove(smallest)
        ss.append(smallest)
    return ss

print(ssort0([3, 5, 4, 2]))
print(ssort1([3, 5, 4, 2]))
print(ssort2([3, 5, 4, 2]))
print(ssort3([3, 5, 4, 2]))
