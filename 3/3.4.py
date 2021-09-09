max_num = int(input())
result = set(range(1, max_num+1))

std_in = input()
while(std_in != "HELP"):
    guess = set(map(int, std_in.split()))
    reply = input()

    if(reply == "YES"):
        result &= guess
    else:
        result -= guess

    std_in = input()

print(*sorted(result))
