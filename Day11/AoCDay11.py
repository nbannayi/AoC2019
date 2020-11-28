'''
Advent of Code 2019 - Day 11
'''

from IntCodeComputer import *
from Point import * 

comp = IntCodeComputer()
comp.load_program_file('AoCDay11input.txt')

def paint_hull(inputs):

    point = Point(0,0)
    angle = 0

    while comp.current_instruction != '99':

        outputs = comp.run_program(inputs, display = False)
        if len(outputs) == 0: break

        # Paint current grid location.
        hull_grid[point] = outputs[0]

        # Work out new point.
        if int(outputs[1]) == 0:
            angle = (angle - 90) % 360
        else:
            angle = (angle + 90) % 360

        #print('Angle',angle, point,'Input',inputs,'Output',outputs)

        if abs(angle) == 0:
            point = Point(point.X, point.Y-1)
        elif abs(angle) == 90:
            point = Point(point.X+1, point.Y)
        elif abs(angle) == 180:
            point = Point(point.X, point.Y+1)
        elif abs(angle) == 270:
            point = Point(point.X-1, point.Y)

        # Work out colour of next grid point to pass in
        if point in hull_grid.keys():
            inputs[0] = hull_grid[point]
        else:
            # Or, add new point
            hull_grid[point] = '0'
            inputs[0] = '0'

    return hull_grid

# Part 1
inputs = [0]
hull_grid = dict()
hull_grid = paint_hull(inputs)

print('Part 1 - at least', len(hull_grid),'squares visited.')
            
# Part 2
print('Part 2 - registration is below:')
inputs = [1]
comp.reset()
hull_grid = paint_hull(inputs)

for row in range(0, 6):

    for col in range(1, 40):

        point = Point(col, row)

        if point in hull_grid.keys():
            if int(hull_grid[point]) == 0:
                print('.', end = '')
            else:
                print('#', end = '')
        else:
            print('.', end = '')

    print('\n', end = '')


    
    
    





    
