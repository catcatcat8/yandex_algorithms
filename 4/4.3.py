words = {}
with open ('input.txt') as f:
    for line in f:
        string = list(line.split())
        for word in string:
            if (word not in words):
                words[word] = 0
            words[word] += 1

result = dict()  # {3: [ddd, wqq]}
for word in words:
    if (words[word] not in result):
        result[words[word]] = [word]
    else:
        result[words[word]].append(word)

list_keys = sorted(list(result.keys()), reverse=True)
for key in list_keys:
    values = sorted(result[key])
    for value in values:
        print(value)
