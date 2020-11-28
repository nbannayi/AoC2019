'''
Advent of Code 2019 - Day 1
'''

file = open( 'AoCDay1Input.txt', 'r' )

modules = []

for module in file:
    modules.append( int( module ) )

file.close()

''' Part 1
'''

total_fuel = 0

for module in modules:
    total_fuel += module // 3 - 2

print( 'Total mass of fuel required in part 1 is: ', total_fuel ) 

'''Part 2
'''

total_fuel = 0
grand_total_fuel = 0

for module in modules:
    fuel = module

    while (fuel > 0):
        fuel = fuel // 3 - 2

        if (fuel <= 0):
            break

        total_fuel += fuel

    grand_total_fuel += total_fuel

print( 'Total mass of fuel required in part 2 is: ', total_fuel ) 



