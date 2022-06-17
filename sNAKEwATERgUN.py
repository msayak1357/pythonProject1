import random
options =["S","W","G"]

your_points=0
my_points=0
no_of_chances=0
chances =10
while (no_of_chances<10):
    your_choice =input("Enter the weapon of your choice Snake =S,Water =W,Gun=G")
    choice= random.choice(options)
    if your_choice=='S' and choice=='W':
        print("the snake drinks the water and wins")
        your_points=your_points+1
        print("your point is ",your_points)
        print("my point is ", my_points)
        no_of_chances=no_of_chances+1
        print("no of chances ",no_of_chances)
        print("THE WATER DROWNS THE GUN SO WINS")
        your_points=your_points+1
        print("your point is ",your_points)
        print("my point is ",my_points)
        no_of_chances=no_of_chances+1
        print("no of chances left",no_of_chances)
    elif your_choice=='G' and choice=='S':
        print("THE GUN KILLS THE SNAKE SO WINS")
        your_points=your_points+1
        print("your point is ",your_points)
        print("my point is ",my_points)
        no_of_chances=no_of_chances+1
        print("no of chances left",no_of_chances)
    elif your_choice == 'S' and choice == 'G':
        print("The Snake gets shot by the Gun.. Hehe You Lose!")
        my_points = my_points + 1
        print("Your Points", your_points)
        print("My Points", my_points)
        no_of_chances = no_of_chances + 1
    elif your_choice == 'S' and choice == 'S':
        print("we got 2 snakes.. so its a draw. ")
        print("Your Points", your_points)
        print("My Points", my_points)
        no_of_chances = no_of_chances + 1
    elif your_choice == 'G' and choice=='W':
        print("THE GUN DROWNS IN WATER SO LOSES")
        my_points=my_points+1
        print("my points is ",my_points)
        print("your points is ",my_points)
        no_of_chances=no_of_chances+1
    elif your_choice=='G' and choice=='G':
        print("BOTH GUNS SO DRAW")
        print("my points are",my_points)
        print("your points are",your_points)
        no_of_chances=no_of_chances+1
    elif your_choice=='W'and my_choice=='S':
        print("Water is drunk by snake so loses")
        my_choice=my_choice+1
        print("my points are",my_points)
        print("your points are",your_points)
        no_of_chances=no_of_chances+1
    elif your_choice=='W'and my_choice=='W':
        print("BOTH WATER SO DRAW")
        print("my choices are",my_points)
        print("your choices are",your_points)
        no_of_chances =no_of_chances+1
    else:
        print("")
print("your points",your_points,"my points",my_points)
if your_points>my_points:
    print("You conquered this game.. Congratz")
if my_points>your_points:
    print("You are pathetic.. Congratz")
if no_of_chances==chances:
    print("GAME OVER ^_~")
    quit()







