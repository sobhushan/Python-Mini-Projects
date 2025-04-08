import random
import math

pc = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gb = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
counter = 0
global flag
flag = False


def display(gb):
    for row in range(3):
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        for col in range(3):
            print("|   " + str(gb[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")


def modifyturn(num, turn):
    for i in range(3):
        for j in range(3):
            if num == gb[i][j]:
                gb[i][j] = turn


def check(gb):
    global flag
    for i in range(3):
        if (gb[i][0] == gb[i][1] == gb[i][2]):
            if gb[i][0] == gb[i][1] == gb[i][2] == "X":
                print("\nCongratulations! You Won")
                flag = True
                break
            else:
                print("\nSorry! You Lost :(")
                flag = True
                break
        elif (gb[0][i] == gb[1][i] == gb[2][i]):
            if (gb[0][i] == gb[1][i] == gb[2][i] == "X"):
                print("\nCongratulations! You Won")
                flag = True
                break
            else:
                print("\nSorry! You Lost :(")
                flag = True
                break
        elif (gb[0][0] == gb[1][1] == gb[2][2]):
            if (gb[0][0] == "X"):
                print("\nCongratulations! You Won")
                flag = True
                break
            else:
                print("\nSorry! You Lost :(")
                flag = True
                break
        elif (gb[0][2] == gb[1][1] == gb[2][0]):
            if (gb[1][1] == "X"):
                print("\nCongratulations! You Won")
                flag = True
                break
            else:
                print("\nSorry! You Lost :(")
                flag = True
                break
        elif pc == []:
            print("\n It's a Tie")
            flag = True
        else:
            pass


print("WELCOME TO THE GAME OF TIC-TAC-TOE")
print("----------------------------------")
print("You are 'X' and I am 'O'\n")

while (flag == False):
    #user turn
    if counter % 2 == 0:
        display(gb)
        pick = int(input("\n Choose a number 1-9: "))
        if (pick >= 1 or pick <= 9) and pick in pc:
            modifyturn(pick, "X")
            pc.remove(pick)
            check(gb)

        else:
            print("Invalid Input. Try Again!")
            continue
        counter += 1

    #computer turn
    else:
        while (True):
            copick = random.choice(pc)
            if copick in pc:
                modifyturn(copick, "O")
                pc.remove(copick)
                check(gb)
                counter += 1
                break
