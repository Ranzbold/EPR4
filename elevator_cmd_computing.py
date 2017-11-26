from elevator_gui import update_gui

def calculate_priority(cmd_elevator, cmd_floor, current_state, last_state):
    int_elevator = []
    int_floor = []


    for i in range(len(cmd_elevator)):
        int_elevator.append(int(cmd_elevator[i][1]))   
    for i in range(len(cmd_floor)):
        int_floor.append(int(cmd_floor[i][0])) 

    if not cmd_elevator:
        if cmd_floor:
            next_cmd = cmd_floor[0]
            return next_cmd
        else:
            return 
    else:
        if not (1 < current_state < 6):
            next_cmd = cmd_elevator[0]
            return next_cmd
        else:
            direction = last_state - current_state
            valid_cmd = [0] * len(cmd_elevator)
            if direction < 0:
                for x in range(len(cmd_elevator)):
                    if int_elevator[x] > current_state:
                        valid_cmd[x] = 1
                try:
                    next_cmd_idx = [idx for idx in range(len(cmd_elevator)) if valid_cmd[idx] == 1][0]
                    next_cmd = cmd_elevator[next_cmd_idx]
                    return next_cmd
                except sum(valid_cmd) == 0:
                    next_cmd = cmd_elevator[0]
                    return next_cmd
                    
            elif direction > 0:
                for x in range(len(cmd_elevator)):
                    if int_elevator[x] < current_state:
                        valid_cmd[x] = 1
                try:
                    next_cmd_idx = [idx for idx in range(len(cmd_elevator)) if valid_cmd[idx] == 1][0]
                    next_cmd = cmd_elevator[next_cmd_idx]
                    return next_cmd
                except sum(valid_cmd) == 0:
                    next_cmd = cmd_elevator[0]
                    return next_cmd                  
            else:
                next_cmd = cmd_elevator[0]
                return next_cmd





dictionary = {"K":"1", "E":"2", "1":"3", "2":"4", "3":"5", "4":"6"}   
current_state = [2, 2] #startpoint (needed for calculate_priority)
last_state = [2, 2] 
cmd_floor = []
cmd_A = []
cmd_B = []


usrinput = input('--> ')
commands = usrinput.split(' ')
#evaluate correctness of entry data


if commands[0] != '':
    for cnt in range(len(commands)):
        if  'r' in commands[cnt][1] or 'h' in commands[cnt][1]:
            dict_cmd_floor = dictionary[commands[cnt][0]]
            commands[cnt] = dict_cmd_floor + commands[cnt][1]
            cmd_floor.append(commands[cnt])
        elif ('A') in commands[cnt][0]:
            dict_cmd_elevator = dictionary[commands[cnt][1]]
            commands[cnt] = commands[cnt][0] + dict_cmd_elevator
            cmd_A.append(commands[cnt])
        elif ('B') in commands[cnt][0]:
            dict_cmd_elevator = dictionary[commands[cnt][1]]
            commands[cnt] = commands[cnt][0] + dict_cmd_elevator
            cmd_B.append(commands[cnt])



#implement waiting of 1-3 rounds
    
#make a loop with recursive calling of functions and updating of last_state, current_state
if cmd_A:
    next_A = calculate_priority(cmd_A, cmd_floor, current_state[0], last_state[0])
    if not(next_A):
        next_A = 'A' + str(current_state[0]) 
    #pop task from A and B
if cmd_B:
    next_B = calculate_priority(cmd_B, cmd_floor, current_state[1], last_state[1])
    if not(next_B):
        next_B = 'B' + str(current_state[1])
    #pop task from A and B

try:
    gui_A = int(next_A[0])
    gui_B = int(next_B[0])    
except:
    gui_A = int(next_A[1])
    gui_B = int(next_B[1])
    
update_gui(gui_A, gui_B)

