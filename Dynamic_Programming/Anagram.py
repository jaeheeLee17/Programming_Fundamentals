def anagram(nums_list):
    anagram_db = []
    anagram_result = [[] for i in range(len(nums_list) + 1)]
    label = 0
    for num in nums_list:
        sep_num = list(num)
        sep_num.sort()
        arrange_num = ''.join(sep_num)
        if anagram_db == []:
            anagram_db.append(arrange_num)
            anagram_result[label].append(num)
            label += 1
        else:
            if arrange_num in anagram_db:
                idx = anagram_db.index(arrange_num)
                anagram_result[idx].append(num)
            else:
                anagram_db.append(arrange_num)
                anagram_result[label].append(num)
                label += 1

    for anagram_list in anagram_result:
        if len(anagram_list) <= 1:
            continue
        else:
            for anagram_num in anagram_list:
                print(anagram_num, end=' ')
        print()

input = ['0952', '5239', '1270', '8581', '7458', '3414', '7906', '2356', '4360', '3491', '6232', '5927', '2735', '2509',
'5849', '8457', '9340', '1858', '8602', '5784']
anagram(input)
