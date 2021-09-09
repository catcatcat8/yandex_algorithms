n = int(input())
houses = list(map(int, input().split()))
if (n % 2 == 1):
    print(houses[n // 2])
else:
    first = houses[n // 2 - 1]
    second = houses[n // 2]
    result = (second + first) // 2
    print(result)
