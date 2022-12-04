from collections import defaultdict
lines = [ l.strip('\n') for l in open("day1.txt", "r").readlines() ]
d = defaultdict(int)
idx = 0
for l in lines:
    if l:
        d[idx] += int(l)
    else:
        idx+=1

part1 = max(d.values())
part2 = sum(sorted(d.values(), reverse=True)[:3])
print(part1,part2)
