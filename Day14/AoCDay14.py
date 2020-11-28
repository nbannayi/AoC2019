'''
Advent of Code 2019 - Day 14
'''

import math

def key_elem(key):

    return key.split(' ')[1]

def key_qty(key):

    return int(key.split(' ')[0])

def expand(element):

    multiplier = 1
    spares_list2 = []

    for key in reactions.keys():

        found_key = ''
        ret_elems1 = []
        ret_elems2 = []
            
        if key_elem(key) == key_elem(element):
            found_key = key
            break
            
    if found_key in reactions.keys():
        ret_elems1 = reactions[found_key]

    if found_key != '':
        
        key_q_fk = key_qty(found_key)
        key_q_e = key_qty(element)

        if key_q_fk < key_q_e:
            multiplier = math.ceil(key_q_e / key_q_fk)

        for elem in ret_elems1:
            ret_elems2.append(str(key_qty(elem)*multiplier)+' '+key_elem(elem))

        if key_elem(found_key) in spares_dict.keys():
            spares_dict[key_elem(found_key)] += (multiplier*key_qty(found_key) - key_qty(element))
        else:
            spares_dict[key_elem(found_key)] = (multiplier*key_qty(found_key) - key_qty(element))

        #print(spares_dict)

    return simplify(ret_elems2)

def fully_expanded(elems):

    expanded = True

    for elem in elems:
        if key_elem(elem) not in ores_list:
            expanded = False
            break

    return expanded

def fully_expand(start_elem):

    list_elems = expand(start_elem)

    while not fully_expanded(list_elems):

        list_elems_expanded = []
    
        for elem in list_elems:

            list_elems_expanded = expand(elem)

            if list_elems_expanded == []:
                list_elems_expanded.append(elem)
            
            list_elems.remove(elem)
            list_elems += list_elems_expanded

        list_elems = simplify(list_elems)

    return(list_elems)

def simplify(elems):

    output_elems = {}
    output_list = []
    spare = ''
    i = 0

    for elem in elems:
        key_e = key_elem(elem)
        key_q = key_qty(elem)

        if key_e in output_elems.keys():
            output_elems[key_e] += key_q
        else:
            output_elems[key_e] = key_q
        
        for spare in spares_dict.keys():
            
            if key_e == spare:
                if spares_dict[spare] < key_q:
                    output_elems[key_e] -= spares_dict[spare]
                    spares_dict[spare] = 0
                    #print('ELem partial',key_e,key_q, 'Spare', spare, spares_dict[spare], 'After', key_e, output_elems[key_e])
                    break
                else:
                    output_elems[key_e] = 0
                    spares_dict[spare] -= key_q
                    #print('ELem full',key_e,key_q, 'Spare', spare, spares_dict[spare], 'After', key_e, output_elems[key_e])
                    break

    for key in output_elems.keys():
        elem_string = str(output_elems[key]) + ' ' + key
        
        if output_elems[key] != 0:
            output_list.append(elem_string)

    return output_list

def calculate_ores(elems):

    total_ores = 0

    for elem in elems:
        key_e = key_elem(elem)
        req_q = key_qty(elem)
        avail_q = 0
        ores_q = 0

        for key in ores.keys():
            if key_elem(key) == key_e:
                avail_q = int(key_qty(key))
                ores_q = int(key_qty(ores[key]))
                break

        total_ores += math.ceil(req_q / avail_q) * ores_q

    return total_ores

# Part 1

# Get input data and load into dictionary.
reactions = {}
ores = {}
ores_list = []
spares_dict = {}

file = open('AoCDay14input.txt', 'r' )

for reaction in file:
    arrow_pos = reaction.find('=>')
    key = reaction[arrow_pos+3:].rstrip("\n\r")
    value = reaction[:arrow_pos-1]

    if 'ORE' in value:
        ores[key] = value
        ores_list.append(key_elem(key))
    else:
        reactions[key] = value.split(', ')

file.close()

# Get the fully expanded string
processed_list = fully_expand('1 FUEL')

print(processed_list)

# Now get OREs needed
print('Part 1 - total OREs needed is ',calculate_ores(processed_list))

''' Couldn't get this solution to work for main input (just examples.) '''
''' Looked up alternate Python solution to compare, more work needed on this solution '''
print (114364 - 114125)
