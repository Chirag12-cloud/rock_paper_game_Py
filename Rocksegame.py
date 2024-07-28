#rock paper game 
import random

A = ["rock","paper",'scissor']

while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game Starts...
1 Yes
2 No | Exit                   
                 '''))
    
    if uc==1:
        for a in range(1,6):
            user_input=int(input('''
1 Rock
2 Scissor
3 Paper                               
                                 '''))
            if user_input==1:
                uchoose = "rock"
            elif user_input==2:
                uchoose = "scissor"
            elif user_input==3:
                uchoose = "paper"
            Cchoose=random.choice(A)
            if Cchoose==uchoose:
                print("Computer Value : ",Cchoose)
                print("User value : ",uchoose)
                print("game drow")
                ucount = ucount + 1
                ccount = ccount + 1
            elif(uchoose=="rock" and Cchoose=="scissor") or (uchoose=="paper" and Cchoose=="rock") or (uchoose=="scissor" and Cchoose=="paper"):
                print("Computer Value : ",Cchoose)
                print("User value : ",uchoose)
                print("you win")
                ucount=ucount+1
            else:
                print("Computer Value : ",Cchoose)
                print("User value : ",uchoose)
                print("Computer win")
                ccount=ccount+1
        if ucount==ccount:
            print("final drow...")
            print("user score..",ucount)
            print("coumputer score..",ccount)
        elif ucount>ccount:
            print("final you win...")
            print("user score..",ucount)
            print("coumputer score..",ccount)
        if ucount<ccount:
            print("final computer win...")
            print("user score..",ucount)
            print("coumputer score..",ccount)
                

    else:
        break