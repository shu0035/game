#gui_part2

from tkinter import*
import tkinter.font as font
import time

import tkinter.messagebox

win = Tk()

win.geometry("650x600")

#Frames


click = True
num = 0
chance = False

def resety():
    global num
    for i in range(9):
        butts[i]["text"] = " "
        butts[i]["fg"] = "black"
        butts[i]["bg"] = "white"
    num = 0


button7 = Button(win,text=" ",bg="white",bd=8,width=20,height=10,command=lambda:checker1(button7))

button7.grid(row=0,column=0)
button4 = Button(win,text=" ",bg="white",bd = 8,width=20,height=10,command=lambda:checker1(button4))
button4.grid(row=1,column=0)
button1 = Button(win,text=" ",bg="white",bd=8,width=20,height=10,command=lambda:checker1(button1))
button1.grid(row=2,column=0)
button8 = Button(win,text=" ",bg="white",bd=8,width=20,height=10,command=lambda:checker1(button8))
button5 = Button(win,text=" ",bg="white",bd=8,width=20,height=10,command=lambda:checker1(button5))
button2 = Button(win,text=" ",bg="white",bd=8,width=20,height=10,command=lambda:checker1(button2))
button8.grid(row=0,column=1)
button5.grid(row=1,column=1)
button2.grid(row=2,column=1)
button9 = Button(win,text=" ",bg="white",bd=8,width=20,height=10,command=lambda:checker1(button9))
button6 = Button(win,text=" ",bg="white",bd=8,width=20,height=10,command=lambda:checker1(button6))
button3 = Button(win,text=" ",bg="white",bd=8,width=20,height=10,command=lambda:checker1(button3))
button9.grid(row=0,column=2)
button6.grid(row=1,column=2)
button3.grid(row=2,column=2)


                


lab = Label(win, width = 20, height = 10)
lab.grid(row=2,column=3)
reset = Button(win, text="Play Again", width=10,bd=8, height=5,command = resety)
reset.grid(row=2, column = 3 )

lab2 = Label(win, width = 20, height = 10)
lab2.grid(row=1,column=3)
reset2 = Button(win, text="VS PLAYER",bd=8, width=10, height=5)
reset2.grid(row=1, column = 3 )

lab3 = Label(win,text="You Are Playing Against the Computer", width = 60, height = 5)
lab3.grid(row=3)
lab3.grid(columnspan = 3)


winningPositions = [[1,4,7],[2,5,8],[3,6,9],[1,2,3],[4,5,6],[7,8,9],[1,5,9],[7,5,3]]
butts = [button1,button2,button3,button4,button5,button6,button7,button8,button9]

def checker(buttons):
    global click
    global num
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"

       
        click =False
        num = num + 1
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click =True
        num = num +1

    if num == 9:
        
        for i in range(9):
            butts[i]["bg"] = "yellow"
            butts[i]["fg"] = "black"
        tkinter.messagebox.showinfo("DRAW", "The game has Been TIED")
    for i in winningPositions:
        if butts[i[0]-1]["text"]==butts[i[1]-1]["text"] and butts[i[1]-1]["text"]==butts[i[2]-1]["text"] and butts[i[0]-1]["text"]=="X":
            
            butts[i[0]-1]["bg"] = "blue"
            butts[i[0]-1]["fg"] = "white"
            butts[i[1]-1]["bg"] = "blue"
            butts[i[1]-1]["fg"] = "white"
            butts[i[2]-1]["bg"] = "blue"
            butts[i[2]-1]["fg"] = "white"
            tkinter.messagebox.showinfo("winner", "X has just won the Game")
            
        if butts[i[0]-1]["text"]==butts[i[1]-1]["text"] and butts[i[1]-1]["text"]==butts[i[2]-1]["text"] and butts[i[0]-1]["text"]=="O":
            butts[i[0]-1]["bg"] = "blue"
            butts[i[0]-1]["fg"] = "white"
            butts[i[1]-1]["bg"] = "blue"
            butts[i[1]-1]["fg"] = "white"
            butts[i[2]-1]["bg"] = "blue"
            butts[i[2]-1]["fg"] = "white"
            
            tkinter.messagebox.showinfo("winner", "O has just won the Game")
            
        
        
   
def checker1(buttons):
    global click
    global num
    global chance
    game = True
    if buttons["text"] == " " and click == True:
        buttons["text"] = "O"
        num = num + 1
    
    
    
    for i in winningPositions:
        if butts[i[0]-1]["text"]==butts[i[1]-1]["text"] and butts[i[1]-1]["text"]==butts[i[2]-1]["text"] and butts[i[0]-1]["text"]=="X" :
            
            butts[i[0]-1]["bg"] = "red"
            butts[i[0]-1]["fg"] = "white"
            butts[i[1]-1]["bg"] = "red"
            butts[i[1]-1]["fg"] = "white"
            butts[i[2]-1]["bg"] = "red"
            butts[i[2]-1]["fg"] = "white"
            game = False
            tkinter.messagebox.showinfo("Looser", "You LOOSE")
            
        if butts[i[0]-1]["text"]==butts[i[1]-1]["text"] and butts[i[1]-1]["text"]==butts[i[2]-1]["text"] and butts[i[0]-1]["text"]=="O":
            butts[i[0]-1]["bg"] = "green"
            butts[i[0]-1]["fg"] = "white"
            butts[i[1]-1]["bg"] = "green"
            butts[i[1]-1]["fg"] = "white"
            butts[i[2]-1]["bg"] = "green"
            butts[i[2]-1]["fg"] = "white"
            game = False
            tkinter.messagebox.showinfo("winner", "You WIN")
            
    if num == 5 and game == True:
        
        for i in range(9):
            butts[i]["bg"] = "yellow"
            butts[i]["fg"] = "red"
        
        
        
    for i in winningPositions:
        
        if butts[i[0]-1]["text"] == butts[i[1]-1]["text"] and butts[i[1]-1]["text"]=="X" and butts[i[2]-1]["text"]==" " and chance == False:
            butts[i[2]-1]["text"]="X"
            chance = True
            break
    for i in winningPositions:        
        if butts[i[2]-1]["text"]==butts[i[1]-1]["text"] and butts[i[1]-1]["text"]=="X" and butts[i[0]-1]["text"]==" " and chance == False:
            butts[i[0]-1]["text"]="X"
            chance = True
            break
    for i in winningPositions:
        if butts[i[0]-1]["text"]==butts[i[2]-1]["text"] and butts[i[2]-1]["text"]=="X" and butts[i[1]-1]["text"]==" " and chance == False:
            butts[i[1]-1]["text"]="X"
            chance = True
            break
    for i in winningPositions:
        if butts[i[0]-1]["text"]==butts[i[1]-1]["text"] and butts[i[1]-1]["text"]=="O" and butts[i[2]-1]["text"]==" " and chance == False:
            butts[i[2]-1]["text"]="X"
            chance = True
            break
    for i in winningPositions:
        if butts[i[2]-1]["text"]==butts[i[1]-1]["text"] and butts[i[1]-1]["text"]=="O" and butts[i[0]-1]["text"]==" " and chance == False:
            butts[i[0]-1]["text"]="X"
            chance = True
            break
    for i in winningPositions:
        if butts[i[0]-1]["text"]==butts[i[2]-1]["text"] and butts[i[2]-1]["text"]=="O" and butts[i[1]-1]["text"]==" " and chance == False:
            butts[i[1]-1]["text"]="X"
            chance = True
            break
    for i in winningPositions:
        if butts[i[0]-1]["text"]==butts[i[2]-1]["text"] and butts[i[2]-1]["text"]==" " and butts[i[1]-1]["text"]=="X" and chance == False:
            butts[i[0]-1]["text"]="X"
            chance = True
            break
    
    for i in winningPositions:        
        if butts[i[2]-1]["text"]==butts[i[1]-1]["text"] and butts[i[1]-1]["text"]==" " and butts[i[0]-1]["text"]=="X" and chance == False:
            butts[i[2]-1]["text"]="X"
            chance = True
            break
    for i in winningPositions:
        
        if butts[i[0]-1]["text"] == butts[i[1]-1]["text"] and butts[i[1]-1]["text"]==" " and butts[i[2]-1]["text"]=="X" and chance == False:
            butts[i[0]-1]["text"]="X"
            chance = True
            break    

    if chance == False:
        butts[7]["text"]="X"

    chance = False
    
    for i in winningPositions:
        if butts[i[0]-1]["text"]==butts[i[1]-1]["text"] and butts[i[1]-1]["text"]==butts[i[2]-1]["text"] and butts[i[0]-1]["text"]=="X" and game == True:
            
            
            
            butts[i[0]-1]["bg"] = "red"
            butts[i[0]-1]["fg"] = "white"
            butts[i[1]-1]["bg"] = "red"
            butts[i[1]-1]["fg"] = "white"
            butts[i[2]-1]["bg"] = "red"
            butts[i[2]-1]["fg"] = "white"
            tkinter.messagebox.showinfo("Looser", "You Loose")
            
        if butts[i[0]-1]["text"]==butts[i[1]-1]["text"] and butts[i[1]-1]["text"]==butts[i[2]-1]["text"] and butts[i[0]-1]["text"]=="O" and game == True:
            butts[i[0]-1]["bg"] = "green"
            butts[i[0]-1]["fg"] = "white"
            butts[i[1]-1]["bg"] = "green"
            butts[i[1]-1]["fg"] = "white"
            butts[i[2]-1]["bg"] = "green"
            butts[i[2]-1]["fg"] = "white"
            
            tkinter.messagebox.showinfo("winner", "You Win")
            
    
    if num == 5 and game == True:
        
        for i in range(9):
            butts[i]["bg"] = "yellow"
            butts[i]["fg"] = "red"
        tkinter.messagebox.showinfo("DRAW", "The game has Been TIED")
    
    




win.mainloop()



