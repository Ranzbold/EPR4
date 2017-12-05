__author__ = "6611082: Cedric Reuter, 6317302: Fabian Eichner"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni" 
__credits__ = " "
__email__ = " " 
def update_gui(aufzug1, aufzug2,):
    int_to_level = {1: "K", 2: "E", 3: "1", 4: "2", 5: "3", 6: "4"}   

    if((not 1 <= aufzug1 <= 6) or (not 1 <= aufzug2 <= 6)):
        print("Ungültige Argumenteingabe")
    else:
        levellist1 = []
        levellist2 = []
        for x in range(1, 7):
            if(not aufzug1 == x):
                levellist1.append("Stockwerk: " + int_to_level[x] + " | |")
            else:
                levellist1.append("Stockwerk: " + int_to_level[x] + " |x|")
            if(not aufzug2 == x):
                levellist2.append("| |")
            else:
                levellist2.append("|x|")

        for x in range(5, -1, -1):           
            print(levellist1[x] + "***" + levellist2[x])
