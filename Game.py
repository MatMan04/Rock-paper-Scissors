#Simple rock,paper,scissors game
import random as rd 
import sys
print("ROCK,PAPER,SCISSORS")
x=0
y=0
z=0
for i in range (100):
    print(str(x)+" Wins, "+str(y)+" Losses, "+str(z)+" Ties")
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    move=input()
    if move == "r":
        print("rock versus...")
        random_num=rd.randint(1,3)
        if random_num==1:
            opponent="p"
            print("Paper")
        elif random_num==2:
            opponent="r"
            print("Rock")
        elif random_num==3:
            opponent="s"
            print("Sissors")
        if opponent==move:
            print("It is a tie")
            z=z+1
            continue
        elif opponent=="p":
            print("You lose")
            y=y+1
            continue
        elif opponent=="s":
            print("you win!")
            x=x+1
            continue
    elif move=="p":
        print("paper versus...")
        random_num=rd.randint(1,3)
        if random_num==1:
            opponent="p"
            print("Paper")
        elif random_num==2:
            opponent="r"
            print("Rock")
        elif random_num==3:
            opponent="s"
            print("Sissors")
        if opponent==move:
            print("It is a tie")
            z=z+1
            continue
        elif opponent=="s":
            print("You lose")
            y=y+1
            continue
        elif opponent=="r":
            print("you win!")
            x=x+1
            continue
    elif move =="s":
        print("Sissors versus...")
        random_num=rd.randint(1,3)
        if random_num==1:
            opponent="p"
            print("Paper")
        elif random_num==2:
            opponent="r"
            print("Rock")
        elif random_num==3:
            opponent="s"
            print("Sissors")
        if opponent==move:
            print("It is a tie")
            z=z+1
            continue
        elif opponent=="r":
            print("You lose")
            y=y+1
            continue
        elif opponent=="p":
            print("you win!")
            x=x+1
            continue
    elif move =="q":
        print("Good Bye")
        sys.exit()
    else:
        print("Please type one of r, p, s, or q.")
    


    

