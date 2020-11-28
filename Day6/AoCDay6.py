'''
Advent of Code 2019 - Day 6
'''

# Get input data.
file = open('AoCDay6input.txt', 'r' )
orbitpairs = []

for orbitpair in file:
    orbitpairs.append(orbitpair[0:7])

file.close()

def get_left_planet(orbitpair):
    return orbitpair[0:3]

def get_right_planet(orbitpair):
    return orbitpair[4:7]

def get_planets(planet):

    left_planet = planet
    current_orbitpair = ''
    planets = []
    
    while left_planet != 'COM':

        for orbitpair in orbitpairs:
            if left_planet == get_right_planet(orbitpair):
                current_orbitpair = orbitpair
                break

        left_planet = get_left_planet(orbitpair)  
        planets.append(left_planet)

    return planets

total_orbit_count = 0
processed_planets = []

# Part 1

for orbitpair in orbitpairs:

    #print('Processing orbitpair: ', orbitpair)
    
    left_planet = get_left_planet(orbitpair)
    right_planet = get_right_planet(orbitpair)

    if not(left_planet in processed_planets):
        total_orbit_count += len(get_planets(left_planet))
        processed_planets.append(left_planet)

    if not(right_planet in processed_planets):
        total_orbit_count += len(get_planets(right_planet))
        processed_planets.append(right_planet)

print('Part 1 - total orbits is ', total_orbit_count)

# Part 2

san_orbitpair = ''
you_orbitpair = ''

for orbitpair in orbitpairs:

    right_planet = get_right_planet(orbitpair)

    if right_planet == 'SAN':
        san_orbitpair = orbitpair

    if right_planet == 'YOU':
        you_orbitpair = orbitpair

    if san_orbitpair != '' and you_orbitpair != '':
        break

san_path = set(get_planets(get_right_planet(san_orbitpair)))
you_path = set(get_planets(get_right_planet(you_orbitpair)))
san_you_path = (san_path - you_path).union(you_path - san_path)

print('Part 2 - total orbits between you and Santa is', len(san_you_path))


