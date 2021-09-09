"""y = -x + d,  y = 0, x = 0"""
d = int(input())
xx, xy = list(map(int, input().split()))

if (xx >= 0 and xy >= 0 and xx + xy <= d):
    print(0)
else:
    first = (xx ** 2 + xy ** 2) ** 0.5
    second = ((xx - d) ** 2 + (xy ** 2)) ** 0.5
    third = ((xx ** 2) + (xy - d) ** 2) ** 0.5
    if (min(first, second, third) == first):
        print(1)
    elif (min(first, second, third) == second):
        print(2)
    else:
        print(3)
