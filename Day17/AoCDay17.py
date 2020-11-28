'''
Advent of Code 2019 - Day 17
'''

import IntCodeComputer as icc
import Point as pnt

# Part 1.

# Determine if a given point is an intersection.
def is_intersection(col, row, scaffolds):
    
    # Rule out edge cases.
    if col - 1 < 0 or col + 1 > 40 or \
       row - 1 < 0 or row + 1 > 46:
       return False

    # Check for cross formation.
    if scaffolds[col][row]   == '#' and \
       scaffolds[col+1][row] == '#' and \
       scaffolds[col-1][row] == '#' and \
       scaffolds[col][row-1] == '#' and \
       scaffolds[col][row+1] == '#':
       return True

    # if there are any other scenarios return false.
    return False

# Initialise and run Intcode program to get outputs (Part 1.)
comp = icc.IntCodeComputer()
comp.load_program_file('/Applications/Python 3.8/MyScripts/AoC2019/Day17/AoCDay17input.txt')
comp.run_program(display=False)

# Process all outputs.
row = col = 0
scaffolds = [['.' for  _ in range(50)] for _ in range(50)]
points = []
alignment_sum = 0

for ascii_code in comp.outputs:

    if ascii_code == 10:
        col = 0; row += 1
    else:
        scaffolds[row][col] = chr(ascii_code)
        col += 1
    
# Scaffolding area is cols 0-40, row 0-46]
# Get all intersection points and store in list.
for col in range(47):
    for row in range(41):
        if is_intersection(col,row,scaffolds):
            points.append(pnt.Point(row,col))

# Get alignment sum.
for p in points: 
    alignment_sum += p.X * p.Y

print('Part 1 alignment sum is:', alignment_sum)

# Part 2.

# Program required:

line_1 = 'A , B , A , B , A , C , B , C , A, C' # overall sequence.
line_2 = 'L , 10 , L , 12 , R , 6'
line_3 = 'R , 10 , L , 4 , L , 4 , L , 12'
line_4 = 'L , 10 , R , 10 , R , 6 , L , 4'

def get_intcode_sequence(input):
    output = []        
    
    for token in str.split(input, ' '):
        if token in ['L', 'R', 'A', 'B', 'C', ',']:
            output.append(ord(token))
        else:
            for c in token: 
                output.append(ord(c))            

    output.append(10)
    return output

combined_input = get_intcode_sequence(line_1) + get_intcode_sequence(line_2) + \
                 get_intcode_sequence(line_3) + get_intcode_sequence(line_4) + [110,10] # n = 110,10 (110), y = 121,10 (121)   

comp.reset()
comp.load_memory_address(0, 2)
comp.run_program(inputs=combined_input, ascii_mode=True)

print()
print('Part 2 vacuumed dust:',comp.outputs[-1])




