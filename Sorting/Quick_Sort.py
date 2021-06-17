def partition(pivot, s):
    left, right = [], []
    for x in s:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return left, right

def qsort(s):
    if len(s) > 1:
        pivot = s[0]
        (left, right) = partition(pivot, s[1:])
        return qsort(left) + [pivot] + qsort(right)
    else:
        return s

# print(qsort([3, 7, 8, 5, 2, 1, 9, 5, 4]))
