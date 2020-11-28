'''
Point class
'''

class Point:
    '''Point object containing an x and y coordinate to show a location in 2D space.'''

    count = 0

    def __init__( self, x = 0, y = 0 ):
        self.X = x
        self.Y = y
        Point.count += 1

    def __eq__(self, other): 
        if not isinstance(other, Point):
            # Don't attempt to compare against unrelated types
            return NotImplemented

        return self.X == other.X and self.Y == other.Y

    def getXLocation( self ):
        return self.X
    
    def getYLocation( self ):
        return self.Y

    def getManhattan( self ):
        return abs(self.Y) + abs(self.X)

    def __str__(self):
        return 'Point (' + str(self.X) + ', ' + str(self.Y) + ')'

    def __hash__(self):
        return hash(str(self.X) + ':' + str(self.Y))



