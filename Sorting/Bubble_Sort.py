def bsort(s):
    for k in range(1, len(s)):
        for i in range(len(s) - k):
            if s[i] > s[i + 1]:
                s[i], s[i + 1] = s[i + 1], s[i]
    return s

# print(bsort([32, 23, 18, 7, 11, 99, 55]))
