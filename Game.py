#Simple rock,paper,scissors game
import random as rd 
import sys
print("ROCK,PAPER,SCISSORS")
x=0
y=0
z=0
#random move for computer
def opponent(move):
    if move==1:
        return "Rock"
    elif move==2:
        return "Paper"
    elif move==3:
        return "Scissors"
for i in range (100):
#will count number of wins,lossesand ties
    print(str(x)+" Wins, "+str(y)+" Losses, "+str(z)+" Ties")
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
#player type move
    move=input()
#player choose rock
    if move == "r":
        print("Rock versus...")
        r=rd.randint(1,3)
        move_2=opponent(r)
        print(move_2)
        if move_2=="Rock":
            print("It is a tie")
            z=z+1
            continue
        elif move_2=="Paper":
            print("You lose")
            y=y+1
            continue
        elif move_2=="Scissors":
            print("you win!")
            x=x+1
            continue
#player choose paper
    elif move=="p":
        print("Paper versus...")
        r=rd.randint(1,3)
        move_2=opponent(r)
        print(move_2)
        if move_2=="Paper":
            print("It is a tie")
            z=z+1
            continue
        elif move_2=="Scissors":
            print("You lose")
            y=y+1
            continue
        elif move_2=="Rock":
            print("you win!")
            x=x+1
            continue
#player choose scissors
    elif move =="s":
        print("Sissors versus...")
        r=rd.randint(1,3)
        move_2=opponent(r)
        print(move_2)         
        if move_2=="Scissors":
            print("It is a tie")
            z=z+1
            continue
        elif move_2=="Rock":
            print("You lose")
            y=y+1
            continue
        elif move_2=="Paper":
            print("you win!")
            x=x+1
            continue
#player choose to quit
    elif move =="q":
        print("Good Bye")
        sys.exit()
#player type another words
    else:
        print("Please type one of r, p, s, or q.")
    


    

