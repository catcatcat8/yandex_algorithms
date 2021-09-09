base_str = input()
len_str = len(base_str)
if (len_str == 1):
    print(0)
else:
    if (len_str % 2 == 1):
        middle = len_str // 2
        index = 1
        coincidences = 0
        
        for i in range(0, middle):
            if (base_str[middle - index] == base_str[middle + index]):
                coincidences += 1
            index += 1

        print(middle - coincidences)
    
    else:
        middle_low, middle_high = len_str // 2 - 1, len_str // 2
        index = 0
        coincidences = 0

        for i in range(0, middle_high):
            if (base_str[middle_low - index] == base_str[middle_high + index]):
                coincidences += 1
            index += 1

        print(middle_high - coincidences)
