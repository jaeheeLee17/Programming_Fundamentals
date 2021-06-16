def isleapyear(year):
    return 0 if year < 0 else ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)

# test case
for y in range(5):
    print(y, isleapyear(y))
for y in range(2010, 2017):
    print(y, isleapyear(y))
for y in range(1900, 2600, 100):
    print(y, isleapyear(y))
