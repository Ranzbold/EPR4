def update_gui(aufzug1, aufzug2,):
    if((not 1 <= aufzug1 <= 6) or (not 1 <= aufzug2 <= 6)):
        print("Ungültige Argumenteingabe")
    else:
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
            print(levellist1[x] + "***" + levellist2[x])
    
update_gui(3,7)
