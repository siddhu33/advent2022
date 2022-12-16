import re    
import sys
import heapq
import itertools
from collections import defaultdict
ptn = re.compile("Valve (.*) has flow rate=(.*); (.*) valve(.*)")

valves = {}

class Valve:
    def __init__(self, name, flow_rate, connections):
        self.name = name
        self.flow_rate = flow_rate
        self.open = False
        self.connections = connections


def shortest_path(start, end):
    open_node = [(0, start)]
    mins = {}
    closed = set()
    while open_node:
        node = heapq.heappop(open_node)
        if node[1] == end:
            return node[0]
        
        options = valves[node[1]].connections
        for val in options:
            nscore = node[0] + 1
            if val not in mins or nscore < mins[val]:
                mins[val] = nscore
                heapq.heappush(open_node, (nscore, val))
                        
        closed.add(val)
    
    return 999

def main():
    sensors = []
    xmin, ymin = sys.maxsize, sys.maxsize
    xmax, ymax = -sys.maxsize, -sys.maxsize
    max_dist = 0
    for line in open("day16/day16.txt", "r").readlines():
        name, flow_rate, _plural, connections = re.match(ptn, line.rstrip("\n")).groups()
        connections = connections.partition(" ")[-1].split(", ")
        flow_rate = int(flow_rate)
        valves[name] = Valve(name, flow_rate, connections)

    pairs = itertools.combinations(valves, 2)
    paths = { tuple(sorted([start,end])): shortest_path(start, end) for start,end in pairs }
    for v in valves:
        paths[(v,v)] = 0
    
    time = 26
    start = valves['AA']
    all_pressure = 0
    opened = []
    to_search = [ v for v in valves.values() if not v.open and v.flow_rate != 0 ]
    #out = get_pressures(paths, start, time, to_search, [])
    out = get_pressures_2(paths, start, time, to_search, [])
    print(out)
    
pressure_map = defaultdict(int)
pressure_map_2 = defaultdict(int)

def to_str(name, time, opened):
    return f"{name}|{time}|{''.join(opened)}"

def get_pressures(paths, node, time, to_search, opened, level=0):
    if time == 0:
        return 0
    if to_str(node.name, time, tuple(opened)) in pressure_map:
        return pressure_map[to_str(node.name, time, tuple(opened))]

    open_valves = ( (v.name, v.flow_rate) for v in to_search if v.flow_rate != 0 and v.name not in opened )
    time_to_travel = ( (v, f, paths[tuple(sorted([node.name,v]))]) for v, f in open_valves )
    pressure_opened = [((time - (t + 1)) * f, t+1, v) for v,f,t in time_to_travel if (t+1) <= time ]
    if not pressure_opened:
        return 0
    pressures = []
    for pressure, travel, new_node in pressure_opened:
        new_opened = opened + [new_node]
        pressures.append( pressure + get_pressures(paths, valves[new_node], time-travel, to_search, new_opened, level+1) )
    max_val = max(pressures)
    pressure_map[to_str(node.name, time, tuple(opened))] = max_val
    return max_val

def get_pressures_2(paths, node1, time, to_search, opened, level=0):
    if time == 0:
        return 0
    if to_str(node1.name, time, tuple(opened)) in pressure_map_2:
        return pressure_map_2[to_str(node1.name, time, tuple(opened))]
    open_valves1 = ( (v.name, v.flow_rate) for v in to_search if v.flow_rate != 0 and v.name not in opened )
    time_to_travel1 = ( (v, f, paths[tuple(sorted([node1.name,v]))]) for v, f in open_valves1 )
    pressure_opened1 = [((time - (t + 1)) * f, t+1, v) for v,f,t in time_to_travel1 if (t+1) <= time ]
    if not pressure_opened1:
        return 0
    pressures = []
    for pressure, travel, new_node in pressure_opened1:
        new_opened = opened + [new_node]
        elephant_traversal = get_pressures_2(paths, valves[new_node], time-travel, to_search, new_opened, level+1)
        my_traversal = get_pressures(paths, valves["AA"], 26, to_search, new_opened, level+1)
        pressures.append( pressure + max(elephant_traversal, my_traversal) )

    max_pressure = max(pressures)
    pressure_map_2[to_str(node1.name, time, tuple(opened))] = max_pressure
    if len(pressure_map_2) % 10 == 0:
        print(f"{len(pressure_map_2)} in pressure map 2")
    return max_pressure


def get_pressure_opened(paths, to_search, time, start):
    open_valves = ( (v.name, v.flow_rate) for v in to_search if not v.open and v.flow_rate != 0 )
    time_to_travel = ( (v, f, paths[tuple(sorted([start.name,v]))]) for v, f in open_valves if start.name )
    pressure_opened = [ ((time - (t + 1)) * f, t+1, v) for v,f,t in time_to_travel if (t+1) <= time ]
    return sorted(pressure_opened, key=lambda x : x[0]/x[1], reverse=True)
        



        
    
                
        
        
        
            
    
    
    

if __name__ == "__main__":
    main()
    