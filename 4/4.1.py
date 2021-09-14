result = {}
n = int(input())
for i in range(0, n):
    colour, value = list(map(int, input().split()))
    if (colour not in result):
        result[colour] = 0
    result[colour] += value

list_keys = sorted(list(result.keys()))
for key in list_keys:
    print(f'{key} {result[key]}')
