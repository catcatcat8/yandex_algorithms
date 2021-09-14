candidates = {}
with open ('input.txt') as f:
    for line in f:
        candidate, votes = line.split()[0], int(line.split()[1])

        if (candidate not in candidates):
            candidates[candidate] = 0
        candidates[candidate] += votes

list_keys = sorted(list(candidates.keys()))
for key in list_keys:
    print(f'{key} {candidates[key]}')
