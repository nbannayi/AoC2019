'''
Advent of Code 2019 - Day 2
'''

def reset_memory():

    file = open( 'AoCDay2Input.txt', 'r' )

    for intcode in file:
        intcodes = intcode.split(sep = ',')

    file.close()

    return intcodes

def compute(noun, verb):

    intcodes = reset_memory()

    intcodes[1] = noun
    intcodes[2] = verb

    i = 0
    intcode = 0

    while( intcode != 99 ):
        intcode = int(intcodes[i])

        if intcode == 99:
            break
        else:
            operand1 = int(intcodes[int(intcodes[i+1])])        
            operand2 = int(intcodes[int(intcodes[i+2])])
            position = int(intcodes[i+3])

            if intcode == 1:
                result = operand1 + operand2
            else:
                result = operand1 * operand2

            intcodes[position] = result
        
            i += 4

    return intcodes[0]

''' Part 1
'''

print( 'At position 1 after program halts is left: ', compute(12, 2) )


''' Part 2
'''

for noun in range (0,99):
    for verb in range (0,99):
        
        if compute(noun, verb) == 19690720:
            print('Answer to part 2 is: ', 100 * noun + verb)
            noun = 100
            break



        
