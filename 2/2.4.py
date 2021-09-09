stdin = list(map(int, input().split()))
bench, legs_amount = stdin[0], stdin[1]

legs = list(map(int, input().split()))

if (bench % 2 == 1):
    middle = bench // 2
    if (middle in legs):
        print(middle)
    else:
        max_less_middle = 0
        min_higher_middle = 10001
        for block in legs:
            if (block < middle and block > max_less_middle):
                max_less_middle = block
            elif (block > middle and block < min_higher_middle):
                min_higher_middle = block
        print(max_less_middle, min_higher_middle)
else:
    middle = bench / 2 - 0.5
    max_less_middle = 0
    min_higher_middle = 10001
    for block in legs:
        if (block < middle and block > max_less_middle):
            max_less_middle = block
        elif (block > middle and block < min_higher_middle):
            min_higher_middle = block
    print(max_less_middle, min_higher_middle)
