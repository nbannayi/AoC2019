'''
IntCodeComputer class.
'''

class IntCodeComputer:
    ''' Class that implements an IntCode computer.'''

    count = 0

    def __init__(self, memory = 10000):
        IntCodeComputer.count += 1

        self.memory = memory
        self.intcodes = [' ' for x in range(self.memory)]        
        self.instruction_pointer = 0
        self.input_pointer = 0
        self.outputs = []
        self.relative_base = 0
        self.program_file = ''
        self.inputs = []

    def load_memory_address(self, address, value):
        ''' Load a specific value in a memory address '''
        self.intcodes[address] = value

    def load_program_file(self, programfile):
        ''' Load computer program from a file. '''

        file = open(programfile, 'r' )

        i = 0
        self.intcodes = [' ' for x in range(self.memory)]   

        for intcode_line in file:
            for intcode in intcode_line.split(sep = ','):
                self.intcodes[i] = intcode
                i += 1

        self.instruction_pointer = 0
        self.input_pointer = 0
        self.outputs = []
        self.relative_base = 0
        self.program_file = programfile

        file.close()

    def load_program_string(self, programstring):
        ''' Load computer program from a string. '''
        
        i = 0
        self.intcodes = [' ' for x in range(self.memory)]   

        for intcode in programstring.split(sep = ','):
            self.intcodes[i] = intcode
            i += 1

        self.instruction_pointer = 0
        self.input_pointer = 0
        self.outputs = []
        self.relative_base = 0 

    def print_memory(self, address_start = -1, address_end = -1):
        ''' Print computer memory. '''

        if address_start == -1 and address_end == -1:
            address_start = 0
            address_end = len(self.intcodes)
        elif address_end == -1:
            address_end = address_start + 1
        
        for address in range(address_start, address_end):

            if self.intcodes[address] == ' ':
                continue

            if self.instruction_pointer == address:
                ip = ' <- Instruction Pointer'
            else:
                ip = ''
        
            print('Address',address,':',self.intcodes[address], ip)
            
    def reset(self):
        ''' Reset the computer (clears the memory.) '''
        
        self.load_program_file(self.program_file)

    def current_instruction(self):
        ''' Get current instruction referenced by the instruction pointer '''

        return self.intcodes[self.instruction_pointer]

    def run_program(self, inputs = [], display = True, ascii_mode = False):
        ''' Run program stored in memory. '''

        if ascii_mode: display = False

        intcode = 0
        self.outputs = []
        self.input_pointer = 0
        
        while int(intcode) != 99 and self.instruction_pointer < len(self.intcodes):
            intcode = self.intcodes[self.instruction_pointer]
            ret = self.process_intcode(intcode, inputs, display, ascii_mode)

            if ret < 0: break

        return self.outputs
        
    def process_intcode(self, intcode, inputs = [], display = True, ascii_mode = False):
        ''' Process current intcode (note this references the current address pointer.) '''

        # Turn into a zero padded 5 char string and unpack
        str_intcode = str(intcode).zfill(5)
        opcode = str_intcode[-2:]
        param1_mode = int(str_intcode[-3])
        param2_mode = int(str_intcode[-4])
        param3_mode = int(str_intcode[-5])

        # NOP instruction.
        if opcode == '00':
            
            return 0     

        # Add and multiply instructions.
        if opcode == '01' or opcode == '02':

            ''' Process operands '''
            self.instruction_pointer += 1
            intcode = self.intcodes[self.instruction_pointer]

            if param1_mode == 0:
                operand1 = self.intcodes[int(intcode)]
            elif param1_mode == 1:
                operand1 = intcode
            else:
                operand1 = self.intcodes[int(intcode) + self.relative_base]
            
            self.instruction_pointer += 1
            intcode = self.intcodes[self.instruction_pointer]

            if param2_mode == 0:
                operand2 = self.intcodes[int(intcode)]
            elif param2_mode == 1:
                operand2 = intcode
            else:
                operand2 = self.intcodes[int(intcode) + self.relative_base]

            # Check for blank operands (empty memory), store 0 by default.
            if operand1 == ' ': operand1 = 0
            if operand2 == ' ': operand2 = 0

            ''' Process operation '''
            if opcode == '01':
                result = int(operand1) + int(operand2)
            elif opcode == '02':
                result = int(operand1) * int(operand2)

            ''' Process third parameter '''
            self.instruction_pointer += 1

            if param3_mode == 0:
                intcode = self.intcodes[self.instruction_pointer]
            else:
                intcode = int(self.intcodes[self.instruction_pointer]) + self.relative_base

            self.intcodes[int(intcode)] = result
            self.instruction_pointer += 1

            return 0
            
        # Get input and store at the location stored in the next address.
        if opcode == '03':
                
            # Interrupt execution to resume later.
            if len(inputs) > 0 and self.input_pointer >= len(inputs):
                return -1

            self.instruction_pointer += 1
            
            if len(inputs) > 0:
                user_input = inputs[self.input_pointer]
            else:
                user_input = input( 'Enter input: ')

            if param1_mode == 0:
                self.intcodes[int(self.intcodes[self.instruction_pointer])] = user_input
            else:
                self.intcodes[int(self.intcodes[self.instruction_pointer]) + self.relative_base] = user_input
            
            self.instruction_pointer += 1
            self.input_pointer += 1

            return 0

        # Print output of the location stored in next address.
        if opcode == '04':

            self.instruction_pointer += 1
            intcode = self.intcodes[self.instruction_pointer]

            if param1_mode == 0:
                operand1 = self.intcodes[int(intcode)]
            elif param1_mode == 1:
                operand1 = int(intcode)
            else: 
                operand1 = self.intcodes[int(intcode) + self.relative_base]
                
            if display: 
                print('Output: ', operand1)
            elif ascii_mode:
                if int(operand1) > 255:
                    print(operand1) # Too big to reasonably be ASCII!
                else:
                    print(chr(int(operand1)), end = '')
                    
            self.outputs.append(operand1)
            self.instruction_pointer += 1

            return 0

        # Boolean jumps.
        if opcode == '05' or opcode == '06':

            self.instruction_pointer += 1
            intcode = self.intcodes[self.instruction_pointer]

            if param1_mode == 0:
                operand1 = self.intcodes[int(intcode)]
            elif param1_mode == 1:
                operand1 = intcode
            else:
                operand1 = self.intcodes[int(intcode) + self.relative_base]
                if operand1 == ' ': operand1 = '0' 

            if (opcode == '05' and int(operand1) != 0) or (opcode == '06' and int(operand1) == 0):
                self.instruction_pointer += 1
                intcode = self.intcodes[self.instruction_pointer]

                if param2_mode == 0:
                    operand2 = self.intcodes[int(intcode)]
                elif param2_mode == 1:
                    operand2 = intcode
                else:
                    operand2 = self.intcodes[int(intcode) + self.relative_base]

                self.instruction_pointer = int(operand2)
            else:
                self.instruction_pointer += 2

            return 0          
            
        # Less than or greater than comparison.
        if opcode == '07' or opcode == '08':

            ''' Process operands '''
            self.instruction_pointer += 1
            intcode = self.intcodes[self.instruction_pointer]

            if param1_mode == 0:
                operand1 = self.intcodes[int(intcode)]
            elif param1_mode == 1:
                operand1 = intcode
            else:
                operand1 = self.intcodes[int(intcode) + self.relative_base]
            
            self.instruction_pointer += 1
            intcode = self.intcodes[self.instruction_pointer]

            if param2_mode == 0:
                operand2 = self.intcodes[int(intcode)]
            elif param2_mode == 1:
                operand2 = intcode
            else:
                operand2 = self.intcodes[int(intcode) + self.relative_base]

            if opcode == '07' and int(operand1) < int(operand2):
                result = 1
            elif opcode == '08' and int(operand1) == int(operand2):
                result = 1
            else:
                result = 0
            
            ''' Process third parameter '''
            self.instruction_pointer += 1

            if param3_mode == 0:
                intcode = self.intcodes[self.instruction_pointer]
            else:
                intcode = int(self.intcodes[self.instruction_pointer]) + self.relative_base
     
            self.intcodes[int(intcode)] = result
            self.instruction_pointer += 1

            return 0

        # Adjust relative base.       
        if opcode == '09':

            self.instruction_pointer += 1
            intcode = self.intcodes[self.instruction_pointer]

            if param1_mode == 0:
                operand1 = self.intcodes[int(intcode)]
            elif param1_mode == 1:
                operand1 = intcode
            else:
                operand1 = self.intcodes[int(intcode) + self.relative_base]
            
            self.relative_base += int(operand1)

            self.instruction_pointer += 1

            return 0

        # Halt instruction.
        if opcode == '99':

            return 0
