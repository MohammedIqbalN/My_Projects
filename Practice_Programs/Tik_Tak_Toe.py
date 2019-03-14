def User_Input(Count):
    #method to ask user input

    if Count % 2 == 0:
        Pos = input("Player 1 enter your number: ")
        PosVal.pop(int(Pos))
        PosVal[int(Pos)] = "X"
    else:
        Pos = input("Player 2 enter your number: ")
        PosVal.pop(int(Pos))
        PosVal[int(Pos)] = "O"

    Print_Pos(PosVal)


def Print_Pos(Pos):
    #print player input into board
    print(" " + Pos[7] + " ||  " + Pos[8] + " ||  " + Pos[9] + " ", end='\n')
    print(" " + Pos[4] + " ||  " + Pos[5] + " ||  " + Pos[6] + " ", end='\n')
    print(" " + Pos[1] + " ||  " + Pos[2] + " ||  " + Pos[3] + " ", end='\n')


PosVal = {
    1: " ",
    2: " ",
    3: " ",
    4: " ",
    5: " ",
    6: " ",
    7: " ",
    8: " ",
    9: " ",
}
for i in range(9):
    if i >= 5:
        if (PosVal[1] == PosVal[2] == PosVal[3] == "X") or (PosVal[4] == PosVal[5] == PosVal[6] == "X") or (PosVal[1] == PosVal[4] == PosVal[7] == "X") or (
                PosVal[7] == PosVal[8] == PosVal[9] == "X") or (PosVal[8] == PosVal[5] == PosVal[2] == "X") or (PosVal[9] == PosVal[6] == PosVal[3] == "X") or (
                    PosVal[7] == PosVal[5] == PosVal[3] == "X") or (PosVal[1] == PosVal[5] == PosVal[9] == "X"):
            print("Player 1 WON")
            exit()
        elif (PosVal[1] == PosVal[2] == PosVal[3] == "O") or (PosVal[4] == PosVal[5] == PosVal[6] == "O") or (PosVal[1] == PosVal[4] == PosVal[7] == "O") or (
                PosVal[7] == PosVal[8] == PosVal[9] == "O") or (PosVal[8] == PosVal[5] == PosVal[2] == "O") or (PosVal[9] == PosVal[6] == PosVal[3] == "O") or (
                    PosVal[7] == PosVal[5] == PosVal[3] == "O") or (PosVal[1] == PosVal[5] == PosVal[9] == "O"):
            print("Player 2 WON")
            exit()
        elif i == 9:
            print("Draw")

    User_Input(i)