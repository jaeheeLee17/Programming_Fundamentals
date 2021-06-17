def merge0(left, right):
    if not (left == [] or right == []):
        if left[0] <= right[0]:
            return [left[0]] + merge0(left[1:], right)
        else:
            return [right[0]] + merge0(left, right[1:])
    else:
        return left + right

def merge1(left, right):
    def loop(left, right, ss):
        if not (left == [] or right == []):
            if left[0] <= right[0]:
                ss.append(left[0])
                return loop(left[1:], right, ss)
            else:
                ss.append(right[0])
                return loop(left, right[1:], ss)
        else:
            return ss + left + right
    return loop(left, right, [])

def merge(left, right):
    ss = []
    while not (left == [] or right == []):
        if left[0] <= right[0]:
            ss.append(left[0])
            left = left[1:]
        else:
            ss.append(right[0])
            right = right[1:]
    return ss + left + right

# print(merge0([18, 23, 32], [7, 11, 55, 99]))
# print(merge1([18, 23, 32], [7, 11, 55, 99]))
# print(merge([18, 23, 32], [7, 11, 55, 99]))
