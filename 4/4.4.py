import math

votes_for_parties = {}
amount_in_duma = {}
sum_votes = 0
with open ('input.txt') as f:
    for line in f:
        split_line = list(line.split())
        party = " ".join(split_line[:-1])
        votes = int(split_line[-1])
        votes_for_parties[party] = votes
        sum_votes += votes

total_amount = 0
for party in votes_for_parties:
    amount = votes_for_parties[party] / (sum_votes / 450)
    amount_in_duma[party] = amount
    total_amount += math.floor(amount)

party_winners = []
while (total_amount < 450):
    max = 0
    party_winner = ""
    for party in amount_in_duma:
        if (amount_in_duma[party] % 1 > max and party not in party_winners):
            max = amount_in_duma[party] % 1
            party_winner = party
        elif (amount_in_duma[party] % 1 == max and party not in party_winners):
            if (votes_for_parties[party] > votes_for_parties[party_winner]):
                party_winner = party
    amount_in_duma[party_winner] += 1
    total_amount += 1
    party_winners.append(party_winner)

for party in amount_in_duma:
    print(f'{party} {math.floor(amount_in_duma[party])}')
