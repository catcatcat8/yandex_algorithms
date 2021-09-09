n, i, j = list(map(int, input().split()))
first = abs(j - i) - 1
second = n - first - 2
print(min(first , second))
