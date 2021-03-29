#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# script by HYOUG
                                                                                                        # ASCII art header :
print(
"""
           ___    __      __                    __      __ 
          /   |  / /___  / /_  ____ _      ____/ /___  / /____  __
         / /| | / / __ \/ __ \/ __ `/_____/ __  / __ \/ //_/ / / /
        / ___ |/ / /_/ / / / / /_/ /_____/ /_/ / /_/ / ,< / /_/ /
       /_/  |_/_/ .___/_/ /_/\__,_/      \__,_/\____/_/|_|\__,_/ 
               /_/
                                by HYOUG
""")
sdk = input("Enter the Sudoku grid with empty boxes replaced by 0 : ")                                  # input
sdk = list(map(int, sdk))                                                                               # sudoku setup
sdk = [item if item != 0 else None for item in sdk]                                                     # //

x_list = list(range(9)) * 9                                                                             # X, Y and C lists setup
y_list = [[i] * 9 for i in range(9)]                                                                    # //
y_list = [i for sublist in y_list for i in sublist]                                                     # //
c_list = [[i] + [i] + [i] for i in range(9)]                                                            # //
c_list = [(c_list[i] + c_list[i+1] + c_list[i+2]) * 3 for i in range(0, 9, 3)]                          # //
c_list = [i for sublist in c_list for i in sublist]                                                     # //

sdk = [{"value": sdk[i], "x": x_list[i], "y": y_list[i], "c": c_list[i]} for i in range(81)]            # assembly of the lists X, Y and C with the values of the input

grid_finished = bool()
while not grid_finished:                                                                                # run the loop until the gris is finished
    grid_finished = True                                                                                # declare the grid finished
    for box1 in sdk:                                                                                    # iterate all the boxes into the grid (box1: box for which we are looking for the number)
        if box1["value"] is None:                                                                       # check if box1 is empty
            poss = [1, 2, 3, 4, 5, 6, 7, 8, 9]                                                          # set the 9 possibilities for box1
            for box2 in sdk:                                                                            # iterate all the boxes into the grid a second time (box2: box with which we compare box1)
                if box2["value"] is not None:                                                           # check if box2 is not empty
                    if box2["x"] == box1["x"] or box2["y"] == box1["y"] or box2["c"] == box1["c"]:      # check if box2 is in the same column or same line or same square
                        if box2 != box1:                                                                # check if box2 isn't box1
                            if box2["value"] in poss:                                                   # check if the box2's value is in the box1's possibilities
                                poss.remove(box2["value"])                                              # remove the box2's value from the box1 possibilities

                if not poss:                                                                            # check if there's no possibilities left
                    break                                                                               # break the second loop to short the execution time

            if len(poss) == 1:                                                                          # check if there's only one possibility left for box1
                box1["value"] = poss[0]                                                                 # set the value of box1 to the only one possibility left
            else:                                                                                       # else
                grid_finished = False                                                                   # declare the grid not finished (one of the box is still empty)

                                                                                                        # result display :
print(f"""\n
{sdk[0]["value"]}#{sdk[1]["value"]}#{sdk[2]["value"]}||{sdk[3]["value"]}#{sdk[4]["value"]}#{sdk[5]["value"]}||{sdk[6]["value"]}#{sdk[7]["value"]}#{sdk[8]["value"]}
{sdk[9]["value"]}#{sdk[10]["value"]}#{sdk[11]["value"]}||{sdk[12]["value"]}#{sdk[13]["value"]}#{sdk[14]["value"]}||{sdk[15]["value"]}#{sdk[16]["value"]}#{sdk[17]["value"]}
{sdk[18]["value"]}#{sdk[19]["value"]}#{sdk[20]["value"]}||{sdk[21]["value"]}#{sdk[22]["value"]}#{sdk[23]["value"]}||{sdk[24]["value"]}#{sdk[25]["value"]}#{sdk[26]["value"]}
===================
{sdk[27]["value"]}#{sdk[28]["value"]}#{sdk[29]["value"]}||{sdk[30]["value"]}#{sdk[31]["value"]}#{sdk[32]["value"]}||{sdk[33]["value"]}#{sdk[34]["value"]}#{sdk[35]["value"]}
{sdk[36]["value"]}#{sdk[37]["value"]}#{sdk[38]["value"]}||{sdk[39]["value"]}#{sdk[40]["value"]}#{sdk[41]["value"]}||{sdk[42]["value"]}#{sdk[43]["value"]}#{sdk[44]["value"]}
{sdk[45]["value"]}#{sdk[46]["value"]}#{sdk[47]["value"]}||{sdk[48]["value"]}#{sdk[49]["value"]}#{sdk[50]["value"]}||{sdk[51]["value"]}#{sdk[52]["value"]}#{sdk[53]["value"]}
===================
{sdk[54]["value"]}#{sdk[55]["value"]}#{sdk[56]["value"]}||{sdk[57]["value"]}#{sdk[58]["value"]}#{sdk[59]["value"]}||{sdk[60]["value"]}#{sdk[61]["value"]}#{sdk[62]["value"]}
{sdk[63]["value"]}#{sdk[64]["value"]}#{sdk[65]["value"]}||{sdk[66]["value"]}#{sdk[67]["value"]}#{sdk[68]["value"]}||{sdk[69]["value"]}#{sdk[70]["value"]}#{sdk[71]["value"]}
{sdk[72]["value"]}#{sdk[73]["value"]}#{sdk[74]["value"]}||{sdk[75]["value"]}#{sdk[76]["value"]}#{sdk[77]["value"]}||{sdk[78]["value"]}#{sdk[79]["value"]}#{sdk[80]["value"]}
\n""")