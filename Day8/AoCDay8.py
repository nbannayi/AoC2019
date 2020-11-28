'''
Advent of Code 2019 - Day 8
'''

file = open('AoCDay8input.txt', 'r' )

image_width = 25
image_height = 6

layer_length = image_width * image_height

image_layers = []

while True:

    image_layer = file.read(layer_length)
    if not image_layer:
        break

    image_layers.append(image_layer)

file.close

# Part 1

image_layer_fewest_0s = ''
fewest_0s = layer_length

for image_layer in image_layers:

    no_0s = image_layer.count('0')

    if no_0s < fewest_0s:
        image_layer_fewest_0s = image_layer
        fewest_0s = no_0s

print('Part 1 - Space Image Format result is ', \
      image_layer_fewest_0s.count('1') * image_layer_fewest_0s.count('2'))

# Part 2

image_layer = ''
image = [[' ' for x in range(image_width)] for y in range(image_height)]

for image_layer in image_layers:
    i = 0
    for row in range(0, image_height):
        for col in range(0, image_width):

            if image[row][col] == ' ':
                image[row][col] = image_layer[i]
            elif image[row][col] == '2':
                image[row][col] = image_layer[i]

            i += 1

print('Part 2 - password image is as below:')

for row in range(0, image_height):
    print('')
    for col in range(0, image_width):
        if image[row][col] == '0':
            print(' ', end = '')
        else:
            print('*', end = '')

    
