def board(x,o):                 #this function will print the board
    zero=" X" if x[0] else("O" if o[0] else 0)
    one="X" if x[1] else("O" if o[1] else 1)
    two="X" if x[2] else("O" if o[2] else 2)
    three="X" if x[3] else( "O" if o[3] else 3)
    four="X" if x[4] else("O" if o[4] else 4)
    five="X" if x[5] else("O" if o[5] else 5)
    six="X" if x[6] else("O" if o[6] else 6)
    seven="X" if x[7] else("O" if o[7] else 7)
    eight="X" if x[8] else("O" if o[8] else 8)
   
    print(f"{zero} | {one} | {two}")
    print(f"---------")
    print(f"{three} | {four} | {five}")
    print(f"---------")
    print(f"{six} | {seven} | {eight}")


def checkwin(x,o):     #check for winner
    Wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for w in Wins:
        if x[w[0]]+x[w[1]]+x[w[2]]==3:
            board(x,o)
            print("Hurahh!! X's Win")
            return 1
        if o[w[0]]+o[w[1]]+o[w[2]]==3:
            board(x,o)
            print("Hurahh!! O's Win")
            return 0
    return -1
#main program

print("\n***************************")
print("--------TIC TAC TOE--------")
print("***************************\n")

x=[0,0,0,0,0,0,0,0,0] # this is for X
o=[0,0,0,0,0,0,0,0,0] # this is for O
turn=1
total=0
while total<9:
    board(x,o)
    if turn==1:
       print("X's Turns")
       choice=int(input("Enter Where You Want Cross:-"))
       x[choice]=1

    else:
        print("O's Turns")
        choice=int(input("Enter Where You Want Circle:-"))
        o[choice]=1
    c=checkwin(x,o)
    if c!=-1:
        break
    turn=1-turn
    total+=1
if total==9 and checkwin(x,o)==-1 :
    print("match draw")
print("\n----THANKYOU FOR USING OUR GAME----")
print("------Hope you enjoy it------\n")


    