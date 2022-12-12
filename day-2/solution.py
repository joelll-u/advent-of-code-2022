f = open("input.txt", "r")

# part 1

translate_opp = {'A' : 'R', 'B' : 'P', 'C': 'S'}
translate_you = {'X': 'R', 'Y': 'P', 'Z': 'S'}
wins = {'R': 'S', 'P': 'R', 'S': 'P'}

def win_score(play1, play2):
    if play1 == play2:
        return 3
    elif wins[play2] == play1:
        return 6
    else:
        return 0

def find_score(play1, play2):
    scores = {'R': 1, 'P': 2, 'S': 3}
    return scores[play2] + win_score(play1, play2)

score_sum = 0
for line in f:
    opp = translate_opp[line[0]]
    u = translate_you[line[2]]
    score_sum += find_score(opp, u)
print(score_sum)

# part 2
f.seek(0)

loses = {'R': 'P', 'P': 'S', 'S': 'R'}

def find_optimal(play1, outcome):
    if outcome == 'X':
        return find_score(play1, wins[play1])
    elif outcome == 'Y':
        return find_score(play1, play1)
    else:
        return find_score(play1, loses[play1])

score_sum = 0
for line in f:
    opp = translate_opp[line[0]]
    score_sum += find_optimal(opp, line[2])
print(score_sum)
f.close()
