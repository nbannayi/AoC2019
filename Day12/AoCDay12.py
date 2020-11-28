'''
Advent of Code 2019 - Day 12
'''

from math import gcd # Python versions 3.5 and above
from functools import reduce # Python version 3.x

# Day 9 input.
io_pos = [-4, -14, 8]
europa_pos = [1, -8, 10]
ganymede_pos = [-15, 2, 1]
callisto_pos = [-17, -17, 16]

io_vel = [0, 0, 0]
europa_vel = [0, 0, 0]
ganymede_vel = [0, 0, 0]
callisto_vel = [0, 0, 0]

def move_system():

    for i in range(0, 3):
        
        if io_pos[i] > europa_pos[i]:
            io_vel[i] -= 1
            europa_vel[i] += 1
        elif io_pos[i] < europa_pos[i]:
            io_vel[i] += 1
            europa_vel[i] -= 1

        if io_pos[i] > ganymede_pos[i]:
            io_vel[i] -= 1
            ganymede_vel[i] += 1
        elif io_pos[i] < ganymede_pos[i]:
            io_vel[i] += 1
            ganymede_vel[i] -= 1

        if io_pos[i] > callisto_pos[i]:
            io_vel[i] -= 1
            callisto_vel[i] += 1
        elif io_pos[i] < callisto_pos[i]:
            io_vel[i] += 1
            callisto_vel[i] -= 1

        if europa_pos[i] > ganymede_pos[i]:
            europa_vel[i] -= 1
            ganymede_vel[i] += 1
        elif europa_pos[i] < ganymede_pos[i]:
            europa_vel[i] += 1
            ganymede_vel[i] -= 1

        if europa_pos[i] > callisto_pos[i]:
            europa_vel[i] -= 1
            callisto_vel[i] += 1
        elif europa_pos[i] < callisto_pos[i]:
            europa_vel[i] += 1
            callisto_vel[i] -= 1

        if ganymede_pos[i] > callisto_pos[i]:
            ganymede_vel[i] -= 1
            callisto_vel[i] += 1
        elif ganymede_pos[i] < callisto_pos[i]:
            ganymede_vel[i] += 1
            callisto_vel[i] -= 1

        io_pos[i] += io_vel[i]
        europa_pos[i] += europa_vel[i]
        ganymede_pos[i] += ganymede_vel[i]
        callisto_pos[i] += callisto_vel[i]

def get_energy(moon):

    energy = 0
    
    for i in range(0, 3):
        energy += abs(moon[i])

    return energy

def get_total_energy(moon):

    energy = 0
    
    if moon.lower() == 'io':
        energy = get_energy(io_pos) * get_energy(io_vel)
    elif moon.lower() == 'europa':
        energy = get_energy(europa_pos) * get_energy(europa_vel)
    elif moon.lower() == 'ganymede':
        energy = get_energy(ganymede_pos) * get_energy(ganymede_vel)
    elif moon.lower() == 'callisto':
        energy = get_energy(callisto_pos) * get_energy(callisto_vel)

    return energy    

def get_total_system_energy():

    energy = get_total_energy('io') + \
             get_total_energy('europa') + \
             get_total_energy('ganymede') + \
             get_total_energy('callisto')

    return energy

def display_system():

    print(io_pos, io_vel,'pot:', get_energy(io_pos),'kin:',get_energy(io_vel),'total:',get_total_energy('io'))
    print(europa_pos, europa_vel,'pot:', get_energy(europa_pos),'kin:',get_energy(europa_vel),'total:',get_total_energy('europa'))
    print(ganymede_pos, ganymede_vel,'pot:', get_energy(ganymede_pos),'kin:',get_energy(ganymede_vel),'total:',get_total_energy('ganymede'))
    print(callisto_pos, callisto_vel,'pot:', get_energy(callisto_pos),'kin:',get_energy(callisto_vel),'total:',get_total_energy('callisto'))

def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)

def get_orbit_length(index, target, display = False):
    
    i = 0

    while True:
        
        if i > 0 and io_pos[index] == target[0] and \
            europa_pos[index] == target[1] and \
            ganymede_pos[index] == target[2] and \
            callisto_pos[index] == target[3]:
                if display:
                    print(i+1)
                    display_system()
                    print('\n')
                break

        i += 1
        move_system()    

    return i+1

# Part 1

for step in range(0, 1000):    
    move_system()
        
print('Part 1 - total system energy is', get_total_system_energy())

# Part 2

io_pos = [-4, -14, 8]
europa_pos = [1, -8, 10]
ganymede_pos = [-15, 2, 1]
callisto_pos = [-17, -17, 16]

io_vel = [0, 0, 0]
europa_vel = [0, 0, 0]
ganymede_vel = [0, 0, 0]
callisto_vel = [0, 0, 0]

x_orbit_length = get_orbit_length(0, [-4, 1, -15, -17], False)

io_pos = [-4, -14, 8]
europa_pos = [1, -8, 10]
ganymede_pos = [-15, 2, 1]
callisto_pos = [-17, -17, 16]

io_vel = [0, 0, 0]
europa_vel = [0, 0, 0]
ganymede_vel = [0, 0, 0]
callisto_vel = [0, 0, 0]

y_orbit_length = get_orbit_length(1, [-14, -8, 2, -17], False)

io_pos = [-4, -14, 8]
europa_pos = [1, -8, 10]
ganymede_pos = [-15, 2, 1]
callisto_pos = [-17, -17, 16]

io_vel = [0, 0, 0]
europa_vel = [0, 0, 0]
ganymede_vel = [0, 0, 0]
callisto_vel = [0, 0, 0]

z_orbit_length = get_orbit_length(2, [8, 10, 1, 16], False)

print('Part 2 - number of steps required to repeat state',lcm([x_orbit_length, y_orbit_length, z_orbit_length]))
    

    





