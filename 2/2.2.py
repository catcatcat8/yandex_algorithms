buildings = list(map(int, input().split()))
shops = []

index = 0
for elem in buildings:
    if (elem == 2):
        shops.append(index)
    index += 1

max_distance = 0

index = 0
for house in buildings:
    if (house == 1):
        min = 11
        for shop in shops:
            if (abs(shop - index) < min):
                min = abs(shop - index)
        if (min > max_distance):
            max_distance = min
    index += 1       

print(max_distance)
