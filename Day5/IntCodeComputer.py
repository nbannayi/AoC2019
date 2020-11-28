'''
IntCodeComputer class.
'''

class IntCodeComputer:
    ''' Class that implements an IntCode computer.'''

    count = 0

    def __init__(self):
        IntCodeComputer.count += 1
        self.intcodes = []
        self.instruction_pointer = 0

    def load_program_file(self, programfile):
        ''' Load computer program from a file. '''

        file = open( programfile, 'r' )

        for intcode in file:
            self.intcodes = intcode.split(sep = ',')

        self.instruction_pointer = 0

        file.close()

    def load_program_string(self, programstring):
        ''' Load computer program from a string. '''
        
        self.intcodes = programstring.split(sep = ',')
        self.instruction_pointer = 0

    def print_memory(self, address_start = -1, address_end = -1):
        ''' Print computer memory. '''

        if address_start == -1 and address_end == -1:
            address_start = 0
            address_end = len(self.intcodes)
        elif address_end == -1:
            address_end = address_start + 1
        
        for address in range(address_start, address_end):

            if self.instruction_pointer == address:
                ip = ' <- Instruction Pointer'
            else:
                ip = ''
        
            print('Address',address,':',self.intcodes[address], ip)
            
    def reset(self):
        ''' Reset the computer (clears the memory.) '''
        
        self.intcodes = []
        self.instruction_pointer = 0

    def run_program(self):
        ''' Run program stored in memory. '''

        intcode = 0
        
        while int(intcode) != 99 and self.instruction_pointer < len(self.intcodes):
            intcode = self.intcodes[self.instruction_pointer]
            self.process_intcode(intcode)

        self.instruction_pointer = 0
        
    def process_intcode(self, intcode):
        ''' Process current intcode (note this references the current address pointer.) '''

        # Turn into a zero padded 5 char string and unpack
        str_intcode = str(intcode).zfill(5)
        opcode = str_intcode[-2:]
        param1_mode = int(str_intcode[-3])
        param2_mode = int(str_intcode[-4])
        param3_mode = int(str_intcode[-5])

        # Add and multiply instructions.
        if opcode == '01' or opcode == '02':

            ''' Process operands '''
            self.instruction_pointer += 1
            intcode = self.intcodes[self.instruction_pointer]

            if param1_mode == 0:
                operand1 = self.intcodes[int(intcode)]
            else:
                operand1 = intcode
            
            self.instruction_pointer += 1
            intcode = self.intcodes[self.instruction_pointer]

            if param2_mode == 0:
                operand2 = self.intcodes[int(intcode)]
            else:
                operand2 = intcode
                
            ''' Process operation '''
            if opcode == '01':
                result = int(operand1) + int(operand2)
            elif opcode == '02':
                result = int(operand1) * int(operand2)

            ''' Process third parameter '''
            self.instruction_pointer += 1
            intcode = self.intcodes[self.instruction_pointer]
            self.intcodes[int(intcode)] = result
            self.instruction_pointer += 1
            return
            
        # Get input and store at the location stored in the next address.
        if opcode == '03':
            self.instruction_pointer += 1
            self.intcodes[int(self.intcodes[self.instruction_pointer])] = input( 'Enter input: ')
            self.instruction_pointer += 1
            return

        # Print output of the location stored in next address.
        if opcode == '04':

            self.instruction_pointer += 1
            intcode = self.intcodes[self.instruction_pointer]

            if param1_mode == 0:
                operand1 = self.intcodes[int(intcode)]
            else:
                operand1 = intcode

            print('Output: ', operand1)
            self.instruction_pointer += 1
            return

        # Halt/NOP instruction.
        if opcode == '99' or opcode == '00':
            return      

        # Boolean jumps.
        if opcode == '05' or opcode == '06':

            self.instruction_pointer += 1
            intcode = self.intcodes[self.instruction_pointer]

            if param1_mode == 0:
                operand1 = self.intcodes[int(intcode)]
            else:
                operand1 = intcode

            if (opcode == '05' and int(operand1) != 0) or (opcode == '06' and int(operand1) == 0):
                self.instruction_pointer += 1
                intcode = self.intcodes[self.instruction_pointer]

                if param2_mode == 0:
                    operand2 = self.intcodes[int(intcode)]
                else:
                    operand2 = intcode

                self.instruction_pointer = int(operand2)
            else:
                self.instruction_pointer += 2

            return                
            
        # Less than or greater than comparison
        if opcode == '07' or opcode == '08':

            ''' Process operands '''
            self.instruction_pointer += 1
            intcode = self.intcodes[self.instruction_pointer]

            if param1_mode == 0:
                operand1 = self.intcodes[int(intcode)]
            else:
                operand1 = intcode
            
            self.instruction_pointer += 1
            intcode = self.intcodes[self.instruction_pointer]

            if param2_mode == 0:
                operand2 = self.intcodes[int(intcode)]
            else:
                operand2 = intcode

            if opcode == '07' and int(operand1) < int(operand2):
                result = 1
            elif opcode == '08' and int(operand1) == int(operand2):
                result = 1
            else:
                result = 0
            
            ''' Process third parameter '''
            self.instruction_pointer += 1
            intcode = self.intcodes[self.instruction_pointer]
            self.intcodes[int(intcode)] = result
            self.instruction_pointer += 1
            return
    
