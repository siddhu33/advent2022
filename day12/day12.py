import heapq

def process(letter):
    if letter == 'S':
        return 0
    elif letter == 'E':
        return ord('z') - ord('a')
    else:
        return ord(letter) - ord('a')
    

def main():
    start = None
    end = None
    heights = []
    lowest_squares = []
    for x, line in enumerate(open("day12/day12.txt", "r").readlines()):
        heights.append([])
        for y, letter in enumerate(line.rstrip("\n")):
            height = process(letter)
            if height == 0:
                lowest_squares.append((x,y))
            heights[x].append(height)
            if letter == 'S':
                start = (x,y)
            elif letter == 'E':
                end = (x,y)
    
    #part 1
    path = shortest_path(start, end, heights)
    print(path)
    
    path2 = shortest_path_astar(start, end, heights)
    print(path2)
    
    #part 2
    print( min( shortest_path(start_node, end, heights) for start_node in lowest_squares ) )
        
    

def shortest_path(start, end, heights):
    open_node = [(0, start)]
    mins = {}
    closed = set()
    x_bound, y_bound = (len(heights), len(heights[0]))
    while open_node:
        node = heapq.heappop(open_node)
        if node[1] == end:
            return node[0]
        
        x,y = node[1]
        current = heights[x][y]
        options = [(x+1, y), (x-1, y), (x, y+1), (x,y-1)]
        for nx, ny in options:
            if nx >= 0 and nx < x_bound and ny >= 0 and ny < y_bound: #bounded
                if (nx,ny) not in closed and heights[nx][ny] <= current+1: #unvisited and can climb
                    nscore = node[0] + 1
                    if (nx,ny) not in mins or nscore < mins[(nx,ny)]:
                        mins[(nx,ny)] = nscore
                        heapq.heappush(open_node, (nscore, (nx,ny)))
            
                        
        closed.add((x,y))
    
    return 99999999

def shortest_path_astar(start, end, heights):
    open_list = [(0, 0, start)]
    x_bound = len(heights)
    y_bound = len(heights[0])
    closed_list = []
    while open_list:
        q = heapq.heappop(open_list)
        x,y = q[2]
        current = heights[x][y]
        options = [(x+1, y), (x-1, y), (x, y+1), (x,y-1)]
        for nx, ny in options:
            new_node = (nx,ny)
            if nx >= 0 and nx < x_bound and ny >= 0 and ny < y_bound: #bounded
                if heights[nx][ny] <= current+1: #unvisited and can climb
                    if new_node == end:
                        return q[1] + 1
                    else:
                        gscore = q[1]+1
                        hscore = abs(end[0]-nx) + abs(end[1]-ny)
                        fscore = gscore + hscore
                        smaller_open = any( n for fs, gs, n in open_list if fs < fscore and n == new_node )
                        smaller_close = any( n for fs, gs, n in closed_list if fs < fscore and n == new_node )
                        if not (smaller_open or smaller_close):
                            heapq.heappush(open_list, (fscore, gscore, new_node))
                            
        closed_list.append(q)
                    
                    

if __name__ == "__main__":
    main()