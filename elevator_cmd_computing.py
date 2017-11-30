import random
from elevator_gui import update_gui

def calculate_priority(cmd_elevator, cmd_floor, current_state, last_state):
    
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



def halt(next_step, cmd_elevator, cmd_floor):
    #check whether people want to get in/out at current floor
    coincidence = False
    for i in range(len(cmd_elevator)):
        if str(next_step) in cmd_elevator[i]:
            cmd_elevator.pop(i)
            coincidence = True
            break
        
    for i in range(len(cmd_floor)):
        if str(next_step) in cmd_floor[i]:
            cmd_floor.pop(i)
            coincidence = True
            break
            
    if coincidence == True:
        wait_parameter = random.randint(1,4)
    else:
        wait_parameter = 0
    
    return wait_parameter, cmd_elevator, cmd_floor
    




dictionary = {"K":"1", "E":"2", "1":"3", "2":"4", "3":"5", "4":"6"}   
current_state = [2, 2] #startpoint (needed for calculate_priority)
last_state = [2, 2] 
cmd_floor = []
cmd_A = []
cmd_B = []
wait_A = 0
wait_B = 0


for turn in range(10):
    
    usrinput = input('--> ')
    commands = usrinput.split(' ')
    #evaluate correctness of entry data
    
    
    if commands[0] != '':
        for cnt in range(len(commands)):
            #distribute commands among lists and convert them from K-4 to 1-6
            if  'r' in commands[cnt][1] or 'h' in commands[cnt][1]:
                dict_cmd_floor = dictionary[commands[cnt][0]]
                commands[cnt] = dict_cmd_floor + commands[cnt][1]
                if commands[cnt] not in cmd_floor:
                    cmd_floor.append(commands[cnt])
            elif ('A') in commands[cnt][0]:
                dict_cmd_elevator = dictionary[commands[cnt][1]]
                commands[cnt] = commands[cnt][0] + dict_cmd_elevator
                if commands[cnt] not in cmd_A:
                    cmd_A.append(commands[cnt])
            elif ('B') in commands[cnt][0]:
                dict_cmd_elevator = dictionary[commands[cnt][1]]
                commands[cnt] = commands[cnt][0] + dict_cmd_elevator
                if commands[cnt] not in cmd_B:
                    cmd_B.append(commands[cnt])
    
    
    if wait_A == 0:
        [next_A, cmd_floor] = calculate_priority(cmd_A, cmd_floor, current_state[0], last_state[0])
    else:
        next_A = current_state[0]
        
    [wait_A, cmd_A, cmd_floor] = halt(next_A, cmd_A, cmd_floor)
        
        
    if wait_B == 0:
        [next_B, cmd_floor] = calculate_priority(cmd_B, cmd_floor, current_state[1], last_state[1])
    else:
        next_B = current_state[1]
        
    [wait_B, cmd_B, cmd_floor] = halt(next_B, cmd_B, cmd_floor)
    
    
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
