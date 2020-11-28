'''
Advent of Code 2019 - Day 7
'''

from IntCodeComputer import *

# Part 1

amp_a = IntCodeComputer()
amp_b = IntCodeComputer()
amp_c = IntCodeComputer()
amp_d = IntCodeComputer()
amp_e = IntCodeComputer()

configs = []

for a in range(0, 5):
    for b in range(0, 5):
        if b == a: continue
        for c in range(0, 5):
            if c == b or c == a: continue
            for d in range (0, 5):
                if d == c or d == b or d == a: continue
                for e in range(0, 5):
                    if e == d or e == c or e == b or e == a: continue
                    configs.append(str(a)+str(b)+str(c)+str(d)+str(e))
    
def init_amp(amp):
    amp.load_program_file('AoCDay7input.txt')

highest_signal = 0

for config in configs:

    a = int(config[0])
    b = int(config[1])
    c = int(config[2])
    d = int(config[3])
    e = int(config[4])
    
    init_amp(amp_a)
    outputs = amp_a.run_program([a,0], False)

    init_amp(amp_b)
    outputs = amp_b.run_program([b,outputs[0]], False)

    init_amp(amp_c)
    outputs = amp_c.run_program([c,outputs[0]], False)

    init_amp(amp_d)
    outputs = amp_d.run_program([d,outputs[0]], False)

    init_amp(amp_e)
    outputs = amp_e.run_program([e,outputs[0]], False)

    if outputs[0] > highest_signal:
        highest_signal = outputs[0]

print('Part 1 - highest signal that can be sent to the thrusters is ', highest_signal)    

# Part 2

configs = []

for a in range(5, 10):
    for b in range(5, 10):
        if b == a: continue
        for c in range(5, 10):
            if c == b or c == a: continue
            for d in range (5, 10):
                if d == c or d == b or d == a: continue
                for e in range(5, 10):
                    if e == d or e == c or e == b or e == a: continue
                    configs.append(str(a)+str(b)+str(c)+str(d)+str(e))

highest_signal = 0

for config in configs:

    # Load program.
    init_amp(amp_a)
    init_amp(amp_b)
    init_amp(amp_c)
    init_amp(amp_d)
    init_amp(amp_e)

    a = int(config[0])
    b = int(config[1])
    c = int(config[2])
    d = int(config[3])
    e = int(config[4])

    # Start amp a input.
    outputs = amp_a.run_program([a,0],False)
    outputs = amp_b.run_program([b,outputs[0]],False)
    outputs = amp_c.run_program([c,outputs[0]],False)
    outputs = amp_d.run_program([d,outputs[0]],False)
    outputs = amp_e.run_program([e,outputs[0]],False)

    while True:
    
        if len(outputs) == 0: break
        outputs = amp_a.run_program([outputs[0]],False)

        if len(outputs) == 0: break
        outputs = amp_b.run_program([outputs[0]],False)

        if len(outputs) == 0: break        
        outputs = amp_c.run_program([outputs[0]],False)

        if len(outputs) == 0: break
        outputs = amp_d.run_program([outputs[0]],False)

        if len(outputs) == 0: break
        outputs = amp_e.run_program([outputs[0]],False)

    if amp_e.outputs[0] > highest_signal:
        highest_signal = amp_e.outputs[0]

print('Part 2 - highest signal from feedback amplifiers is ', highest_signal)

