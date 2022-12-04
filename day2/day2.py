import sys

# A - Rock, B - Paper, C - Scissors
# X - Rock, Y - Paper, Z - Scissors

mapping = { 'A' : 'Y', 'B' : 'Z', 'C' : 'X' }
scores = { 'A' : 1, 'B' : 2, 'C': 3, 'X' : 1, 'Y': 2, 'Z': 3 }
pairs = [ l.rstrip("\n").split() for l in open(sys.argv[1], 'r').readlines() ]
calculated = ( (theirs, ours, mapping[theirs], scores[theirs], scores[ours]) for theirs, ours in pairs )
round_scores = []
for theirs, ours, expected, score1, score2 in calculated:
    if expected == ours:
        round_scores.append((score1+0, score2+6))
    elif score1 == score2:
        round_scores.append((score1+3, score2+3))
    else:
        round_scores.append((score1+6, score2+0))

print(sum(ours for theirs, ours in round_scores))
part2_score = 0
them_win = { 'A' : 'Z', 'B': 'X', 'C': 'Y' }
draw = { 'A' : 'X', 'B' : 'Y', 'C': 'Z' }
for theirs, ours in pairs:
    if ours == 'X':
        part2_score += (0 + scores[them_win[theirs]])
    elif ours == 'Y':
        part2_score += (3 + scores[theirs])
    elif ours == 'Z':
        part2_score += (6 + scores[mapping[theirs]])
print(part2_score)
