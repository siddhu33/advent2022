import re    
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

ptn = re.compile("Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)")
 
def main():
    sensors = []
    xmin, ymin = sys.maxsize, sys.maxsize
    xmax, ymax = -sys.maxsize, -sys.maxsize
    max_dist = 0
    for line in open("day15/day15.txt", "r").readlines():
        locations = [ int(i) for i in re.match(ptn, line.rstrip("\n")).groups() ]
        sx, sy, bx, by = locations
        xmin = min(xmin, sx, bx)
        xmax = max(xmax, sx, bx)
        ymin = min(ymin, sy, by)
        ymax = max(ymax, sy, by)
        sensor_dist = abs(sx-bx) + abs(sy-by)
        max_dist = max(max_dist, sensor_dist)
        sensors.append([(sx,sy), (bx,by), sensor_dist])
    
    beacons = { x[1] for x in sensors }
    sensor_areas = [ [(s[0]-d, s[1]), (s[0]+d, s[1]), (s[0], s[1]-d), (s[0], s[1]+d)] for s,b,d in sensors ]
    sensor_lines = [ [ (a[0], a[3]), (a[3], a[1]), (a[1], a[2]), (a[2], a[0]) ] for a in sensor_areas ]
    offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    xrange = 4000000
    yrange = 4000000
    try:
        for lines, sensor_data in zip(sensor_lines, sensors):
            sensor, beacon, distance = sensor_data
            for idx, pair in enumerate(lines):
                begin, end = pair
                offset = offsets[idx]
                start = begin
                xdelta = 1 if (end[0] - begin[0]) > 0 else -1
                ydelta = 1 if (end[1] - begin[1]) > 0 else -1
                while start != end:
                    point = start[0] + offset[0], start[1] + offset[1]
                    if 0 <= point[0] <= xrange and 0 <= point[1] <= yrange:
                        distances = [ abs(s[0] - point[0]) + abs(s[1] - point[1]) - d for s,b,d in sensors ]
                        if not any( d < 1 for d in distances ):
                            print(point[0], point[1], 4000000*point[0]+point[1])
                            raise StopIteration()
                    start = start[0] + xdelta, start[1] + ydelta
    except StopIteration:
        print("found!")




    # y_coord = 2000000 
    # no_sensors = 0
    # x_coord = xmin - max_dist
    # while x_coord <= xmax + max_dist:
    #     smaller = False
    #     for sensor, _beacon, distance in sensors:
    #         point_dist = abs(sensor[0] - x_coord) + abs(sensor[1] - y_coord)
    #         if point_dist <= distance:
    #             smaller = True
    #             break
    #     if smaller and (x_coord,y_coord) not in beacons:
    #         no_sensors +=1 
    #     x_coord += 1

    # print(no_sensors)
                
        
        
        
            
    
    
    

if __name__ == "__main__":
    main()
    