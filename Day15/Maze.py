'''
Maze class.
'''

from tkinter import *
from Point import *
from IntCodeComputer import *
import tkinter.messagebox as box

class MazeCreator:
    ''' Class that draws a Maze with an Ascii display.'''

    count = 0

    def __init__(self, size, program_file):
        MazeCreator.count += 1

        self.window = Tk()        
        self.program_file = program_file
        self.window.title('Maze creator')
        self.previous_position = Point(0,0)
        self.directions = []
        self.oxygen_minutes = 0
        self.next_blocks = [Point(12,12)]
        self.oxygen_filled = []

        self.size = size
        self.trail_steps = 0
        self.trail_last_position = Point(0,0)
        self.inputs = [0]
        self.position = Point(0,0)
        self.cpu = IntCodeComputer()
        self.cpu.program_file = program_file
        self.cpu.reset()
        
        self.window.bind_all(',', self.keypress)
        self.window.bind_all('.', self.keypress)
        self.window.bind_all('a', self.keypress)
        self.window.bind_all('z', self.keypress)
        self.window.bind_all('s', self.keypress)
        self.window.bind_all('o', self.keypress)

        self.display = [[' ' for i in range(-size, size+1)] for j in range(-size, size+1)]

        self.visited = []

        box.showinfo('Advent of Code 2019 - Day 15', 'This is the solution to Oxygen tank. '+ \
                     'Use A, Z, < and > keys to move up, down, left and right.  S key to draw maze '+ \
                     ' and O key to fill maze with oxygen once fully drawn.')

    def keypress(self, event):

        ch = event.char

        if ch == ".":
            self.inputs[0] = 4
        elif ch == ",":
            self.inputs[0] = 3
        elif ch == 'a':
            self.inputs[0] = 1
        elif ch == 'z':
            self.inputs[0] = 2
        elif ch == 's':
            self.traverse_maze()
            print('Part 1 - 208 steps to oxygen tank.')
            return
        elif ch == 'o':
            self.next_blocks = self.fill_oxygen(self.next_blocks)
            print('Part 2 - Maze takes',self.oxygen_minutes,'minutes to fill with oxygen.')
            return

        response = self.cpu.run_program(self.inputs, False)[0]

        self.position = self.process_input(response, self.position)

    def traverse_maze(self):

        maze_exists = True

        while maze_exists: 
            self.depth_first_search()
            maze_exists = self.backtrack()

    def fill_oxygen(self, blocks):

        next_blocks = []
        still_filling = False
        
        for current_block in blocks:

            n_block = Point(current_block.X, current_block.Y-1)
            s_block = Point(current_block.X, current_block.Y+1)
            w_block = Point(current_block.X-1, current_block.Y)
            e_block = Point(current_block.X+1, current_block.Y)

            if n_block in self.visited and \
               n_block not in self.oxygen_filled:
                still_filling = True
                next_blocks.append(n_block)
                self.draw(n_block, 'oxygen')
                self.oxygen_filled.append(n_block)

            if s_block in self.visited and \
                s_block not in self.oxygen_filled:
                still_filling = True
                next_blocks.append(s_block)
                self.draw(s_block, 'oxygen')
                self.oxygen_filled.append(s_block)

            if w_block in self.visited and \
                w_block not in self.oxygen_filled:
                still_filling = True
                next_blocks.append(w_block)
                self.draw(w_block, 'oxygen')
                self.oxygen_filled.append(w_block)

            if e_block in self.visited and \
                e_block not in self.oxygen_filled:
                still_filling = True
                next_blocks.append(e_block)
                self.draw(e_block, 'oxygen')
                self.oxygen_filled.append(e_block)
        
        if still_filling:
            self.oxygen_minutes += 1
            self.fill_oxygen(next_blocks)

        return next_blocks
    
    def process_input(self, response, position):
        
        if response == 0:
            self.draw_maze(self.inputs[0], position, 'wall')
        elif response == 1:
            self.update_loc_colour('black', position)
            position = self.draw_maze(self.inputs[0], position, 'trail')
            self.update_loc_colour('red', position)
        elif response == 2:
            position = self.draw_maze(self.inputs[0], position, 'tank')
            print('Oxygen is at position ', position)

        return position

    def update_loc_colour(self, colour, position):

        col = position.X + self.size
        row = position.Y + self.size        

        if self.display[col][row] != ' ':            
            if colour == 'black':
                self.display[col][row].configure(foreground = "black")
                self.display[col][row].configure(background = "white")
            else:
                self.display[col][row].configure(foreground = "red")
                self.display[col][row].configure(background = "red")                

    def draw_maze(self, direction, position, block_type):

        block_position = Point(0,0)
        
        # Draw block in direction we're facing
        if direction == 1:
            block_position = Point(position.X, position.Y-1)
        elif direction == 2:
            block_position = Point(position.X, position.Y+1)
        elif direction == 3:
            block_position = Point(position.X-1, position.Y)
        elif direction == 4:
            block_position = Point(position.X+1, position.Y)

        self.draw(block_position, block_type)

        return block_position
            
    def draw(self, point, block_type):
        ''' Update the maze. '''

        col = point.X + self.size
        row = point.Y + self.size

        if self.display[col][row] == ' ':

            if block_type == 'wall':
                self.display[col][row] = Label(self.window, font = 'Verdana 5', text = ' ')
            elif block_type == 'trail':
                self.display[col][row] = Label(self.window, font = 'Verdana 5', text = '.')
            elif block_type == 'tank':
                self.display[col][row] = Label(self.window, font = 'Verdana 5', text = 'O')
                
            self.display[col][row].grid(row = row, column = col, padx = (1,1), pady = (1,1))

        if block_type == 'wall':
            self.display[col][row].configure(background="black")
            self.display[col][row].configure(foreground="white")
        elif block_type == 'trail':
            self.display[col][row].configure(background="white")
            self.display[col][row].configure(foreground="black")
        elif block_type == 'tank':
            self.display[col][row].configure(background="green")
            self.display[col][row].configure(foreground="white")            
        elif block_type == 'oxygen':
            self.display[col][row].configure(background="green")
            self.display[col][row].configure(foreground="white")

    def get_neighbouring_directions(self):

        neighbouring_directions = []

        for direction in range(1,5):
            self.inputs[0] = direction
            response = self.cpu.run_program(self.inputs, False)[0]

            if response == 1 or response == 2:

                if direction == 1:
                    self.inputs[0] = 2
                elif direction == 2:
                    self.inputs[0] = 1
                elif direction == 3:
                    self.inputs[0] = 4
                elif direction == 4:
                    self.inputs[0] = 3

                if response == 2:
                    self.oxygen_tank_position = self.position
                
                self.cpu.run_program(self.inputs, False)[0]
                neighbouring_directions.append(direction)
            else:
                self.process_input(response, self.position)

        return neighbouring_directions

    def depth_first_search(self):

        self.visited.append(self.position)
        self.previous_position = self.position
        neighbours = self.get_neighbouring_directions()

        for direction in neighbours:

            block_position = Point(0,0)

            if direction == 1:
                block_position = Point(self.position.X, self.position.Y-1)
            elif direction == 2:
                block_position = Point(self.position.X, self.position.Y+1)
            elif direction == 3:
                block_position = Point(self.position.X-1, self.position.Y)
            elif direction == 4:
                block_position = Point(self.position.X+1, self.position.Y)

            if block_position not in self.visited:
                self.inputs[0] = direction
                response = self.cpu.run_program(self.inputs, False)[0]
                self.position = self.process_input(response, self.position)
                if self.previous_position == self.position:
                    return
                else:
                    self.directions.append(direction)
                    self.depth_first_search()
                
    def backtrack(self):
        new_direction = 0

        while len(self.directions) > 0:

            direction = self.directions.pop()

            if direction == 1:
                new_direction = 2
            elif direction == 2:
                new_direction = 1
            elif direction == 3:
                new_direction = 4
            elif direction == 4:
                new_direction = 3

            self.inputs[0] = new_direction
            response = self.cpu.run_program(self.inputs, False)[0]
            self.position = self.process_input(response, self.position)

            neighbours = self.get_neighbouring_directions()

            for dire in neighbours:

                if dire == 1:
                    block_position = Point(self.position.X, self.position.Y-1)
                elif dire == 2:
                    block_position = Point(self.position.X, self.position.Y+1)
                elif dire == 3:
                    block_position = Point(self.position.X-1, self.position.Y)
                elif dire == 4:
                    block_position = Point(self.position.X+1, self.position.Y)

                if block_position not in self.visited:
                    return True
        
        return False
    
           

                
            
            
        
  


