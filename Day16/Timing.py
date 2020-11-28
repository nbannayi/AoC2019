'''
Advent of Code 2019 - Day 16
'''

from timeit import default_timer as timer

with open('AoCDay16input.txt', 'r' ) as file:
    phase_input_str = file.read().strip()

start = timer()

for n in range(0,650*10000):
    pass

end = timer()
print(end-start)
