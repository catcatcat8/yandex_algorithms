mas = []

mas.append(int(input()))
max = mas[0]

while(mas[-1] != 0):
    next = int(input())
    mas.append(next)
    if (next > max):
        max = next

result = 0
for item in mas:
    if (item == max):
        result += 1

print(result)
