lst = list(map(int, input().split()))

not_dublicates = list()
dublicates = set()
for num in lst:
    if(num not in not_dublicates):
        not_dublicates.append(num)
    else:
        dublicates.add(num)

for num in lst:
    if (num not in dublicates):
        print(num)
