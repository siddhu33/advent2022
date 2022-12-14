import copy

VAL_MAP = {
    0 : '.',
    1 : 'o',
    2 : '#'
}

def print_cave(cave, fname="cave"):
    with open(f"{fname}.txt", "w") as f:
        for line in cave:
            f.write(''.join(VAL_MAP[v] for v in line))
            f.write("\n")

def next_loc(cave, grain_loc):
    y,x = grain_loc
    if y >= len(cave)-1:
        return None
    
    if cave[y+1][x] == 0:
        return y+1,x
    elif cave[y+1][x-1] == 0:
        return y+1,x-1
    elif cave[y+1][x+1] == 0:
        return y+1,x+1
    
def pour_sand(cave, floor=999):
    ys, xs = 0, 500
    grains = 0
    pouring = True
    while pouring:
        grain_loc = ys, xs
        while grain_loc := next_loc(cave, grain_loc):
            prev_loc = grain_loc
        if prev_loc[0] != floor:
            cave[prev_loc[0]][prev_loc[1]] = 1
            grains += 1
        else:
            pouring = False
            
    return grains
            
def pour_till_blocked(cave):
    ys, xs = 0, 500
    grains = 0
    while cave[0][500] != 1:
        grain_loc = ys, xs
        prev_loc = ys, xs
        while grain_loc := next_loc(cave, grain_loc):
            prev_loc = grain_loc
        
        cave[prev_loc[0]][prev_loc[1]] = 1
        grains += 1        
            
    return grains
    
 
def main():
    cave = [ [0 for j in range(1000)] for i in range(1000) ]
    y,x = len(cave), len(cave[0])
    maxy = 0
    for group in open("day14/day14.txt", "r").read().split("\n"):
        edges = [ tuple(int(i) for i in i.split(",")) for i in group.split(" -> ") ]
        for idx, edge in enumerate(edges[:-1]):
            next_edge = edges[idx+1]
            x0, y0 = edge
            x1, y1 = next_edge
            maxy = max(maxy, y0, y1)
            sx0, sx1 = sorted([x0, x1])
            sy0, sy1 = sorted([y0, y1])
            for j in range(sy0, sy1+1):
                for i in range(sx0, sx1+1):
                    cave[j][i] = 2
    
    cave2 = copy.deepcopy(cave)
    grain_count = pour_sand(cave)
    print(grain_count)
    for i in range(len(cave2[maxy+2])):
        cave2[maxy+2][i] = 2
        
    grains_till_blocked = pour_till_blocked(cave2)
    print(grains_till_blocked)
    
    print_cave(cave)
    print_cave(cave2, "cave2")
    
    

if __name__ == "__main__":
    main()
    