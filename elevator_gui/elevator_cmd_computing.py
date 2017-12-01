"""This code enables a twin elevator to processes calls from the floors and within the elevators, \
and visualizes their current states.
"""

import random
import itertools
import string
from elevator_gui import update_gui

__author__ = "6611082: Cedric Reuter, 6317302: Fabian Eichner"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni" 
__credits__ = " "
__email__ = " " 


def calculate_priority(cmd_elevator, cmd_floor, current_state, last_state):
    """Calculating the momentary target of the elevator and giving back the next elevator \
    position. Needs the commands from the elevator and the floors as input as well as the \
    state information about the current and previous postion of the elevator.
    """
    int_elevator = []
    int_floor = []

    #transforming to integers
    for i in range(len(cmd_elevator)):
        int_elevator.append(int(cmd_elevator[i][1]))   
    for i in range(len(cmd_floor)):
        int_floor.append(int(cmd_floor[i][0])) 

    #calculate priority destination for elevator
    if not cmd_elevator:
        if cmd_floor:
            next_cmd = int_floor[0]
            cmd_floor.pop(0)
        else:
            next_cmd = current_state
    else:
        if not (1 < current_state < 6):
            next_cmd = int_elevator[0]
        else:
            direction = last_state - current_state
            valid_cmd = [0] * len(int_elevator)
            if direction < 0:
                for x in range(len(int_elevator)):
                    if int_elevator[x] > current_state:
                        valid_cmd[x] = 1
                #check whether there's a target in the current direction
                if sum(valid_cmd) == 0:
                    next_cmd = int_elevator[0]  
                else:
                    next_cmd_idx = [idx for idx in range(len(int_elevator)) \
                                    if valid_cmd[idx] == 1][0]
                    next_cmd = int_elevator[next_cmd_idx] 
            elif direction > 0:
                for x in range(len(int_elevator)):
                    if int_elevator[x] < current_state:
                        valid_cmd[x] = 1
                #check whether there's a target in the current direction
                if sum(valid_cmd) == 0:
                    next_cmd = int_elevator[0] 
                else:
                    next_cmd_idx = [idx for idx in range(len(int_elevator)) \
                                    if valid_cmd[idx] == 1][0]
                    next_cmd = int_elevator[next_cmd_idx]
                
                   
            else:
                next_cmd = int_elevator[0]
                
    #determine movement of elevator
    if next_cmd > current_state:
        next_step = current_state + 1
    elif next_cmd < current_state:
        next_step = current_state - 1
    elif next_cmd == current_state:
        next_step = current_state
    return next_step, cmd_floor



def halt(next_step, cmd_elevator, cmd_floor, current_state, last_state):
    """Checks whether people want to get in/out at current floor. If this is indeed the case and \
    some requirements are met, it calculates the waiting time for the people to get in/out.
    """
    coincidence = False
    for i in range(len(cmd_elevator)):
        if str(next_step) in cmd_elevator[i]:
            cmd_elevator.pop(i)
            coincidence = True
            break
    
    for i in range(len(cmd_floor)):
        if str(next_step) in cmd_floor[i]:
            if (('r' in cmd_floor[i][1]) and (current_state < last_state)) \
            or (('h' in cmd_floor[i][1]) and (current_state > last_state)):
                cmd_floor.pop(i)
                coincidence = True
                break
            
    if coincidence == True:
        wait_parameter = random.randint(2,4)
    else:
        wait_parameter = 0
    
    return wait_parameter, cmd_elevator, cmd_floor
    
def check_input(input):
    pass

dictionary = {"K":"1", "E":"2", "1":"3", "2":"4", "3":"5", "4":"6"}   
current_state = [2, 2] #startpoint (needed for calculate_priority)
last_state = [2, 2] 
cmd_floor = []
cmd_A = []
cmd_B = []
wait_A = 0
wait_B = 0

for turn in range(10): #should be while loop before we hand it in
    valid_input = False
    letters_elevator = ('A','B')
    letters = ('H','R')
    valid_floor_letters = ('K','E','1','2','3','4')
    valid_cmds = []

    temp_cmds = set(itertools.product(letters_elevator,valid_floor_letters))
    for tuple in temp_cmds:
        valid_cmds.append(tuple[0] + tuple[1])
    temp_cmds = set(itertools.product(valid_floor_letters,letters))
    for tuple in temp_cmds:
        valid_cmds.append(tuple[0] + tuple[1])

    valid_cmds.append('R')
    valid_cmds.append('H')
    valid_cmds.append('')
    valid_cmds.remove('KH')
    valid_cmds.remove('4R')

    while (not valid_input):
        usrinput = input('--> ')
        if (not usrinput.upper() in valid_cmds):
            print("Falsche Eingabe. Gültige Zeichen zur Eingabe: " + str(valid_cmds))
        else:
            valid_input = True

                
        commands = usrinput.split(' ')
    
    #evaluate correctness of entry data
    
    
    if commands[0] != '':
        for cnt in range(len(commands)):
            #distribute commands among lists and convert them from K-4 to 1-6
            #Todo Implement handler for input r and h
            if 'r' in commands[cnt][1] or 'h' in commands[cnt][1]:
                dict_cmd_floor = dictionary[commands[cnt][0]]
                commands[cnt] = dict_cmd_floor + commands[cnt][1]
                if commands[cnt] not in cmd_floor:
                    cmd_floor.append(commands[cnt])
            elif 'A' in commands[cnt][0]:
                dict_cmd_elevator = dictionary[commands[cnt][1]]
                commands[cnt] = commands[cnt][0] + dict_cmd_elevator
                if commands[cnt] not in cmd_A:
                    cmd_A.append(commands[cnt])
            elif 'B' in commands[cnt][0]:
                dict_cmd_elevator = dictionary[commands[cnt][1]]
                commands[cnt] = commands[cnt][0] + dict_cmd_elevator
                if commands[cnt] not in cmd_B:
                    cmd_B.append(commands[cnt])
    
    
    if wait_A == 0:
        [next_A, cmd_floor] = calculate_priority(cmd_A, cmd_floor, current_state[0], last_state[0])
    else:
        next_A = current_state[0]
        
    [wait_A, cmd_A, cmd_floor] = halt(next_A, cmd_A, cmd_floor, current_state[0], last_state[0])
        
        
    if wait_B == 0:
        [next_B, cmd_floor] = calculate_priority(cmd_B, cmd_floor, current_state[1], last_state[1])
    else:
        next_B = current_state[1]
        
    [wait_B, cmd_B, cmd_floor] = halt(next_B, cmd_B, cmd_floor, current_state[1], last_state[1])
    
    
    update_gui(next_A, next_B)
    
    #counter for elevator entry/exit
    if wait_A != 0:
        wait_A -= 1
    if wait_B != 0:
        wait_B -= 1
        
    #update state
    last_state = current_state
    current_state = [next_A, next_B]
    
    print('cmd_A', cmd_A, 'cmd_B', cmd_B, 'cmd_floor', cmd_floor, 'current_state', current_state)
