#Description
#The character will play Lost in a Jungle. The character could be any person from any age. He or 
    #She will be alone in the jungle. The jungle will be full of dangerous animals. The game will ask 
    #first the username. Then the game will call the user by their name and tell them what to do.

#Map
#you are standing in the middle of the jungle surrounded by dangerous animals. As you look for 
    #the way out, you have to move calmly and make decisions wisely. If you scream for help, the animals 
    #could hear you and then come after you. Next, you faced a bear. Your one wrong move can take you to 
    #death. So, you played dead. The bear thought you are dead so it left. Next, you saw a tiger walking by. 
    #Instead of running, you remained calm and backed away slowly and hid. It didn’t see you. Now you 
    #are very hungry, but the jungle is full of poisonous fruits. You saw bananas on a banana tree which 
    #seemed edible. Instead of eating first, you gave it to a rat to try. The rat ate it and he seemed fine. 
    #So, you ate it too! Afterwards, you saw a river. If you cross it, you will be out of the jungle. But the
    #river is full of stonefish. If you swim, they will eat you. You gathered some banana trees and made a boat. Then you 
    #got on the boat and crossed the river without getting eaten by the stonefish. Finally, you are out of the jungle!

import time
#this is the Intoduction function
def gameIntro():
    #this is the introduction
    print()
    print('_____Game Name: Lost in the Jungle!_____')
    print()
    print('''You are lost in a Jungle! This jungle is full of dangerous animals.
You have to use your mind in order to survive and find the way out from the jungle.
While you are stuck in this jungle, you will be given certain hard situations.
All you have to do is to choose the right decisions to get a step
closer to the way out of jungle!
The 1st Four situations worth 10 points each, and the Last situation worth 50 points
At the end, the Game will declare how many points you have earned.
If you earn more than 80 points, you Won! Else, you will be stuck forever!
Choose wisely!''')
    
    print()
    print()
    print('-' * 50 + '>')
    time.sleep(2)
    return

# First situation
def ChoiceOne(name, point):
    
    print(name + ''', you  are lost in the jungle now!
What would you do to find your way out of the jungle first of all?''')

    #Options
    options =( "1. I will scream for help", "2. I will calmly find the way out", "3. I will gather all the animals")
    for i in options:
        print(i)

    print()
    Choice = ''
    while Choice != '1' and Choice != '2' and Choice != '3':
        Choice = input("Choose Wisely from above options 1, 2, or 3: ")
    

    #declare the result
    if Choice == '1':
        point = 0
        print('Sorry, you are stuck!')
        print()
        
    elif Choice == '2':
        point = 10
        print('Yay, that is correct!')
        print()
    else:
        point = 0
        print('Nope, that is a wrong move!')
        print()

    print('-' * 50 + '>')
    time.sleep(2)    
    return point
        
# Secound situation
def ChoiceTwo(name, point):
    print('A bear saw you ' + name + ' and it is comming toward you, what are you going to do now?')

    #options
    options = ("1. I will play dead", "2. I will run", "3. I will play with it")
    for i in options:
        print(i)
    print()

    #ask the user to choose
    Choice = ''
    while Choice != '1' and Choice != '2' and Choice != '3':
        Choice = input("Choose Wisely from above options 1, 2, or 3: ")

    #declare the result
    if Choice == '1':
        point = 10
        print('Yup, absolutely right!')
        print("Bears don't eat dead people")
        print()
        
    elif Choice == '2':
        point = 0
        print('Nope, it will come after you!')
        print()
    else:
        point = 0
        print('Nope, it will eat you!')
        print()
    print('-' * 50 + '>')
    time.sleep(2)
    return point
        
# Third situation
def ChoiceThree(name, point):
    print(name + ', a Tiger is walking by you! What are you going to do now?')
    options = ("1. I will try to hide", "2. I will run", "3. I will play dead")
    for i in options:
        print(i)
    print()
    
    #ask the user to choose
    Choice = ''
    while Choice != '1' and Choice != '2' and Choice != '3':
        Choice = input("Choose Wisely from above options 1, 2, or 3: ")

    #declare the result
    if Choice == '1':
        point = 10
        print('Yup, great move!')
        print()
        
    elif Choice == '2':
        point = 0
        print('Nope, it will chase you!')
        print()
    else:
        point = 0
        print('Nope, it will still eat you!')
        print()
    print('-' * 50 + '>')
    time.sleep(2)
    return point

# Fourth situation
def ChoiceFour(name, point):
    print(name + ''', you are very hungry now, but the jungle is full of poisonous fruits!
You saw banana trees and cherry trees. Among them, one kind of fruit is edible!
What is going to be your next move?''')
    options = ("1. I will stay hungry", "2. I will eat them", "3. I will give some banana and cherry to a rat for taste!")
    for i in options:
        print(i)
    print()
    
    #ask the user to choose
    Choice = ''
    while Choice != '1' and Choice != '2' and Choice != '3':
        Choice = input("Choose Wisely from above options 1, 2, or 3: ")

    #declare the result
    if Choice == '1':
        point = 0
        print('Nope, you will get weaker and will not be able to find the way out')
        print()
        
    elif Choice == '2':
        point = 0
        print('No, you will die if you eat the one that is poisonous')
        print()
    else:
        point = 10
        print('Right, you can figure out the edible fruit by watching which fruit the rat is eating.')
        print('If you see the rat is fine after eating banana, then you can eat it too!')
        print()
    print('-' * 50 + '>')
    time.sleep(2)
    return point

# Fifth situation
def ChoiceFive(name, point):
    print('''Finally, you see a river. You can get out of the jungle if you cross it!
However, the river is full of stonefish. What are you going to do now?''')
    options = ("1. I will swim!", "2. I will make a boat with banana trees and cross the river!", "3. I will live in the jungle forever!")
    for i in options:
        print(i)
    print()
    
    #ask the user to choose
    Choice = ''
    while Choice != '1' and Choice != '2' and Choice != '3':
        Choice = input("Choose Wisely from above options 1, 2, or 3: ")

    #declare the result
    if Choice == '1':
        point = 0
        print('Wrong, stonefish will eat you!')
        print()
        
    elif Choice == '2':
        point = 60
        print('Yay, You are free from the Jungle ' + name)
        print()
    else:
        point = 0
        print('Nope, you will not survive in this dangerous jungle!')
        print()
    print('=' * 70)
    print()
    time.sleep(2)
    return point

#This is the Game function which will carry the introduction of the game,
#and questions along with the result!
def Game():
    #Declare variables
    Qone = str()
    Qtwo = str()
    Qthree = str()
    Qfour = str()
    Qfive = str()
    name = str()
    total = int()
     
    #Ask for username
    name = input("What is your name: ")


    point = ''
    

    #Display
    #the game will declare the results here 
    #whether the user has found the way out of jungle or not!
    Intro = gameIntro()
    Qone = ChoiceOne(name, point)
    Qtwo = ChoiceTwo(name, point)
    Qthree = ChoiceThree(name, point)
    Qfour = ChoiceFour(name, point)
    Qfive = ChoiceFive(name, point)

    #add the total points
    total = (Qone + Qtwo + Qthree + Qfour + Qfive)

    #declare total points earned
    print("Total points earned: ", total)
    print()
    if total >= 80:
        print('Congratulations! You have won the Game and free from the Jungle')
    else:
        print('Sorry to inform you that you are stuck forever in this Jungle')
    print('!' * 70)
    print()

    
#Ask the user to play again function
def play_again():
    play = input('Do you want to play again? (yes or no): ')
    play = play.upper()

    if play == "YES":
        return True
    else:
        return False

#this is the main function which will state the entir game    
def main():
    #stating the Game
    game = Game()
   
    #ask the user to play again
    while play_again():
        print('_' * 80)
        print()
        Game()
    print('Byeee!!!')

main()
