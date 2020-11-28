'''
Point class
'''

import math

class Point:
    '''Point object containing an x and y coordinate to show a location in 2D space.'''

    count = 0

    def __init__(self, x = 0, y = 0):
        self.X = x
        self.Y = y
        Point.count += 1

    def __eq__(self, other): 
        if not isinstance(other, Point):
            # Don't attempmt to compare against unrelated types
            return NotImplemented

        return self.X == other.X and self.Y == other.Y

    def get_manhattan(self):
        return abs(self.Y) + abs(self.X)

    def get_gradient(self, other_point):

        direction = ' '

        if other_point.Y == self.Y:
            if self.X - other_point.X > 0:
                direction = 'UX'
            else:
                direction = 'DX'
        elif other_point.X == self.X:
            if self.Y - other_point.Y > 0:
                return '0U'
            else:
                return '0D'
        else:
            if (self.Y > other_point.Y and self.X > other_point.X) or \
               (self.Y > other_point.Y and self.X < other_point.X):
                direction = 'UXY'
            else:
                direction = 'DXY'
                
        return str((self.Y - other_point.Y) / (self.X - other_point.X)) + direction

    def get_distance(self, other_point):
        return math.sqrt((other_point.Y - self.Y) ** 2 + (other_point.X - self.X) ** 2)

    def __str__(self):
        return 'Point (' + str(self.X) + ', ' + str(self.Y) + ')'

    def __hash__(self):
        return hash(str(self.X) + ':' + str(self.Y))



