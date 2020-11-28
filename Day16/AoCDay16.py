'''
Advent of Code 2019 - Day 16
'''

from itertools import cycle, accumulate
      
def calculate(phase_input, phase_no):

    phase_input_len = len(phase_input)
    add_list = []
    subtract_list = []

    for n in range(phase_no-1, phase_input_len, phase_no*4):

        for m in range(0, phase_no):
            add = n + m
            if add > phase_input_len - 1:
                break
            else:
                add_list.append(int(phase_input[add]))

        for m in range(0, phase_no):
            subtract = n+2*phase_no+m
            if subtract > phase_input_len - 1:
                break
            else:
                subtract_list.append(int(phase_input[subtract]))

    return str(sum(add_list) - sum(subtract_list))[-1]

def calculate_phase(phase_input):

    phase_output = ''

    for n in range(1, len(phase_input)+1):
        phase_output += calculate(phase_input, n)

    return phase_output

def calculate_phase_n(phase_input, no_phases):

    phase_output = phase_input
    
    for n in range(0, no_phases):
        phase_output = calculate_phase(phase_output)

    return phase_output[0:8]

def calculate_phase_n_pt2(phase_input, no_phases):

    offset = int(phase_input[:7])
    digits = [int(n) for n in phase_input]

    l = 10000 * len(digits) - offset
    
    i = cycle(reversed(digits))
    arr = [next(i) for _ in range(l)]

    # Repeatedly take the partial sums mod 10
    for _ in range(no_phases):
        arr = [n % 10 for n in accumulate(arr)]

    return "".join(str(i) for i in arr[-1:-9:-1])

# Part 1

with open("AoCDay16input.txt") as file:
    phase_input = file.read().strip()
    
phase_output = phase_input
print('Part 1 answer is',calculate_phase_n(phase_output,100))

# Part 2

print('Part 2 answer is',calculate_phase_n_pt2(phase_input, 100))


