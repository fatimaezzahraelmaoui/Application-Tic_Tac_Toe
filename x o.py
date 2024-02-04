from tkinter import *
import random

def next_turn():
    global player
    
    if Buttons[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]:
            Buttons[row][column]["text"] = player
            if check_winner() is False :
                player = players[1]
                label.config(text=(players[1]+" turn"))
            elif check_winner() is True:
                label.config(text=(players[0]+ " wins"))
            elif check_winner() is "Tie":
                    label.config(text=(" Tie!"))
def check_winner():
    for row in range(3):
        if Buttons[row][0]["text"] == Buttons[row][1]["text"] == Buttons[row][2]["text"] != "":
            Buttons[row][0].config(bg="green")
            Buttons[row][1].config(bg="green")
            Buttons[row][2].config(bg="green")
            return True
    
    for column in range(3):
        if Buttons[0][column]["text"] == Buttons[1][column]["text"] == Buttons[2[column]]["text"] != "":
            Buttons[0][column].config(bg="green")
            Buttons[1][column].config(bg="green")
            Buttons[2][column].config(bg="green")
            return True

        if Buttons[0][0]["text"] == Buttons[1][1]["text"] == Buttons[2][2]["text"] != "":
            Buttons[0][0].config(bg="green")
            Buttons[1][1].config(bg="green")
            Buttons[2][2].config(bg="green")
            return True
         
        if Buttons[0][2]["text"] == Buttons[1][1]["text"] == Buttons[2][0]["text"] != "":
            Buttons[0][0].config(bg="green")
            Buttons[1][1].config(bg="green")
            Buttons[2][2].config(bg="green")
            return True 
        
        elif empty_spaces() is False:
            for row in range(3):
                for column in range(3):
                    Buttons[row][column].config(bg="green")
            return "Tie!"
        else:
            return False

def empty_spaces():
    spaces = 9 
    for row in range(3):
        for column in range(3):
            if Buttons[row][column]["text"] != "":
                spaces -= 1
    
    if spaces == 0:
        return False
    else:
        return True

def new_game():
    global player 
    player = random.choice(players)
    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            Buttons[row][column].config(text="" ,bg="#F0F0F0")

window = Tk()
window.title("TIC_TAC")
players = ["X","O"]
player = random.choice(players)
Buttons = [[0,0,0]
           [0,0,0]
           [0,0,0]]
label = label(text="player" + "turn", font=("consolas",40))
label.pack(side="top")

resst_button = Button(txt="restart", command=new_game)
resst_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        Buttons[row][column] = Button(frame, text="",width=5, height=2,command=lambda row=row,column=column:next_turn(row,column))
        Buttons[row][column].grid(row=row, column=column)

