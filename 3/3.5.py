all_guesses = []
all_numbers = []
result = []

count = int(input())
for i in range(0, count):
    guess = input()
    all_guesses.append(guess)

numbers = int(input())
for i in range(0, numbers):
    number = input()
    all_numbers.append(number)

max = -1
for each_num in all_numbers:
    k = 0
    for each_guess in all_guesses:
        if (len(set(each_guess) - set(each_num)) == 0):
            k += 1
    if (k == max):
        result.append(each_num)
    if (k > max):
        max = k
        result.clear()
        result.append(each_num)

[print(num) for num in result]
