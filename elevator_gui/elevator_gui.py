def update_gui(aufzug1, aufzug2,):
    levellist1 = []
    levellist2 = []
    for x in range(1,7):
        if(not aufzug1 == x):
            levellist1.append("| |")
        else:
            levellist1.append("|x|")
        if(not aufzug2 == x):
            levellist2.append("| |")
        else:
            levellist2.append("|x|")

    for x in range(0,6):
        print(levellist1[x] + "*** " + levellist2[x])
    
update_gui(3,5)
