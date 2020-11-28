'''
Advent of Code 2019 - Day 3
'''

from Point import *

#Read Manhattan data into a list.
file = open( 'AoCDay3Input.txt', 'r' )

passthrough = 1

wire1 = []
wire2 = []

for wire in file:
    if (passthrough == 1):
        wire1 = wire.split(sep = ',')
        passthrough += 1
    else:
        wire2 = wire.split(sep = ',')

file.close()

def laywire(wire):

    wirelist = []

    relx = 0
    rely = 0

    for step in wire:
        direction = step[0]
        magnitude = int(step[1:])
        
        if direction == 'R':
            for x in range (relx+1, relx+magnitude+1):
                p = Point(x, rely)
                wirelist.append(p)

            relx += magnitude
        
        elif direction == 'L':
            for x in range (relx-1, relx-magnitude-1, -1):
                p = Point(x, rely)
                wirelist.append(p)

            relx -= magnitude

        elif direction == 'D':
            for y in range (rely-1, rely-magnitude-1, -1):
                p = Point(relx, y)
                wirelist.append(p)

            rely -= magnitude  

        if direction == 'U':
            for y in range (rely+1, rely+magnitude+1):
                p = Point(relx, y)
                wirelist.append(p)

            rely += magnitude

    return wirelist

wirelist1 = laywire(wire1)
wirelist2 = laywire(wire2)

wireset1 = set()
wireset2 = set()

wirecrossset = set()

for point in wirelist1:
    wireset1.add(point)

for point in wirelist2:
    wireset2.add(point)
 
wirecrossset = wireset1.intersection(wireset2)

mostcentral = 0

for point in wirecrossset:
    mh = point.getManhattan()

    if mostcentral == 0 or mostcentral > mh:
        mostcentral = mh

print( 'Manhattan distance from the central port to the closest intersection is', mostcentral)

# part2
leaststeps = 0

for point in wirecrossset:
    nosteps = wirelist1.index(point) + wirelist2.index(point) + 2

    if leaststeps == 0 or leaststeps > nosteps:
        leaststeps = nosteps

print( 'Least steps for an intersection is', leaststeps)
        
    
    
    
