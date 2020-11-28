'''
Advent of Code 2019 - Day 10
'''

from Point import *

file = open('AoCDay10input.txt', 'r' )

asteroid_lines = []

while True:

    asteroid_line = file.readline()
    
    if not asteroid_line:
        break

    asteroid_lines.append(asteroid_line)

file.close

asteroid_grid = set()

row = 0

for asteroid_line in asteroid_lines:
    col = 0 # Reset at start of each row

    for position in asteroid_line:
        if position == '#':
            asteroid_grid.add(Point(col, row))

        col += 1
    row += 1
    
    print(asteroid_line, end = '')

print('\n')

def get_visible_asteroids(asteroid_point, display = False):
    
    gradients = dict()
    chosen_point = asteroid_point

    for point in asteroid_grid:

        if point == asteroid_point: continue

        current_gradient = asteroid_point.get_gradient(point)
        #print(point, current_gradient)

        if current_gradient not in gradients.keys():
            gradients[current_gradient] = {point}
        else:
            gradients[current_gradient].add(point)

    for key in gradients.keys():
        if len(gradients[key]) > 1:

            min_distance = cur_distance = 0
            first_pass = True
            
            for point in gradients[key]:
                cur_distance = asteroid_point.get_distance(point)

                if first_pass or cur_distance < min_distance:
                    first_pass = False
                    min_distance = cur_distance
                    chosen_point = point
            
            gradients[key] = {chosen_point}

    if (display):
        print('There are', len(gradients.keys()),'visible asteroids:')
        for key in gradients.keys():
            for point in gradients[key]:
                print(key, point)
                
    return gradients

# Part 1

max_asteroids = 0
best_location = Point()

for point in asteroid_grid:
    asteroids = get_visible_asteroids(point).values()
    if len(asteroids) >= max_asteroids:
        max_asteroids = len(asteroids)
        best_location = point

print('Part 1 - the best location is', best_location, 'with', max_asteroids, 'visible asteroids')

# Part 2
# Needs hefty refactoring!!!

final_results = []

while len(asteroid_grid) > 1:

    results = []
    asteroids = get_visible_asteroids(best_location)

    # Get first point, 0 degs
    try:
        values = asteroids.get('0U')
        for point in values: results.append(point)
        del asteroids['0U']
    except:
        True

    # First quadrant (-UXY)
    quadrant_list = []
    for key in asteroids.keys():
        if 'UXY' in key and float(key[:-3]) < 0:
            quadrant_list.append(float(key[:-3]))

    quadrant_list.sort()

    for key in quadrant_list:
        for point in asteroids[str(key) + 'UXY']:
            results.append(point)
            del asteroids[str(key) + 'UXY']

    # 90 deg point
    try:
        values = asteroids.get('-0.0DX')
        for point in values: results.append(point)
        del asteroids['-0.0DX']
    except:
        True

    # second quadrant (+DXY)
    quadrant_list = []
    for key in asteroids.keys():
        if 'DXY' in key and float(key[:-3]) > 0:
            quadrant_list.append(float(key[:-3]))

    quadrant_list.sort()

    for key in quadrant_list:
        for point in asteroids[str(key) + 'DXY']:
            results.append(point)
            del asteroids[str(key) + 'DXY']

    # 180 deg point
    values = asteroids.get('0D')
    try:
        for point in values: results.append(point)
        del asteroids['0D']
    except:
        True

    # Third quadrant (-DXY)
    quadrant_list = []
    for key in asteroids.keys():
        if 'DXY' in key and float(key[:-3]) < 0:
            quadrant_list.append(float(key[:-3]))

    quadrant_list.sort()

    for key in quadrant_list:
        for point in asteroids[str(key) + 'DXY']:
            results.append(point)
            del asteroids[str(key) + 'DXY']

    # 270 deg point
    values = asteroids.get('0.0UX')
    try:
        for point in values: results.append(point)
        del asteroids['0.0UX']
    except:
        True

    # Third quadrant (+UXY)
    quadrant_list = []
    for key in asteroids.keys():
        if 'UXY' in key and float(key[:-3]) > 0:
            quadrant_list.append(float(key[:-3]))

    quadrant_list.sort()

    for key in quadrant_list:
        for point in asteroids[str(key) + 'UXY']:
            results.append(point)
            del asteroids[str(key) + 'UXY']

    # Collect final results and destroy asteroids
    for point in results:
        final_results.append(point)

    asteroid_grid -= set(results)

# Output vaporisaed asteroids
answer = final_results[199]
print('Part 2 - 200th asteroid vapourised is',answer,'answer is',int(answer.X*100+answer.Y))

#for i in range(0, len(final_results)):
#    print('Asteroid',i+1,'vapourised', final_results[i])








    
