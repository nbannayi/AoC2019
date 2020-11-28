'''
ArcadeCabinet class.
'''

from IntCodeComputer import *
from tkinter import *
import tkinter.messagebox as box

class ArcadeCabinet:
    ''' Class that implements an ArcadeCabinet with an Ascii display.'''

    count = 0

    def __init__(self, programfile):
        ArcadeCabinet.count += 1

        self.cpu = IntCodeComputer()
        self.program_file = self.cpu.program_file = programfile
        self.cpu.reset()
        self.inputs = [0]
        self.score = 0
        self.blocks = 0

    def keypress(self, event):
        ch = event.char
        if ch == ".":
            self.inputs[0] = 1
        elif ch == ",":
            self.inputs[0] = -1
        else:
            self.inputs[0] = 0

        outputs = self.cpu.run_program(self.inputs, False)
        ret = self.process_outputs(outputs)

        # Game over!
        if ret == 1:
            box.showinfo( 'Game over!', 'You scored '+str(self.score)+ '.')
            sys.exit()
            
    def play(self):
        ''' Play the game '''

        self.window = Tk()
        self.window.bind_all(',', self.keypress)
        self.window.bind_all('.', self.keypress)

        self.display = [[' ' for i in range(1, 51)] for j in range(1, 51)]

        self.window.title('Arcade game - care package')

        self.cpu.load_memory_address(0, 2)
        outputs = self.cpu.run_program(self.inputs, False)
        self.process_outputs(outputs)

        box.showinfo('Advent of Code 2019 - Day 13', 'Welcome to the Care Package arcade game. '+ \
                     'This is the solution for day 13 of Advent of Code 2019.'+ \
                     ' Use < and > keys to move the bat and destroy all blocks.  Good luck!')

        self.window.mainloop()
                            
    def process_outputs(self, inputs):

        i = 0

        if len(inputs) == 0:
            return 1
        
        while self.cpu.current_instruction != '99':
            
            c = int(inputs[i])
            r = int(inputs[i+1])
            block = int(inputs[i+2])

            if c == -1 and r == 0:
                if block != 0:
                    self.score = block
                    self.window.title('Arcade game - care package     Score: '+str(self.score) + \
                                      '  Blocks: '+str(self.blocks))
            else:
                if self.display[c][r] == ' ':
                    self.display[c][r] = Label(self.window, text = ' ')
                    self.display[c][r].grid(row = r, column = c, padx = (1,1), pady = (1,1))

                if block == 0:
                    if self.display[c][r].cget('background') == 'blue':
                        self.blocks -= 1
                        self.window.title('Arcade game - care package     Score: '+str(self.score) + \
                                          '  Blocks: '+str(self.blocks))
                        
                    self.display[c][r].configure(background="white")
                elif block == 1 or block == 3:
                    self.display[c][r].configure(background="black")
                elif block == 4:
                    self.display[c][r].configure(background="red")
                elif block == 2:
                    self.display[c][r].configure(background="blue")
                    self.blocks += 1
                                    
            i += 3

            if i >= len(inputs): break

        return 0



