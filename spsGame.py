import random 

component = ['stone' , 'paper', 'scissors']
count = 0
count2 = 0
for i in range(0,3):
    print(f"these are ur options {component}" )
    userChoice=input("enter what you choice: ")
    pythonChoice= random.choice(component)
    if userChoice == 'stone' and pythonChoice == 'scissors':
        print("congrats computer wins this time :(.")
        count += 1
    elif userChoice == 'scissors' and pythonChoice == 'scissors':
        print('its a tie 0.0')

    elif userChoice == 'paper' and pythonChoice == 'scissors':
        print("oh no python won this time :(")
        count2 += 1
    elif userChoice == 'stone' and pythonChoice == 'stone':
        print("its a tie.")

    elif userChoice == 'scissors' and  pythonChoice == 'stone':
        print('shoot python won ')
        count2 += 1
    elif userChoice == 'paper' and pythonChoice == 'stone':
        print("hey guess what , you won :). ")
        count += 1
    elif userChoice == 'stone' and pythonChoice == 'stone':
        print('its a tie nobody loses.')

    elif userChoice == 'scissors' and pythonChoice == 'paper':
        print('yee, u won ')
        count =+ 1 
    elif userChoice == 'stone' and pythonChoice == 'paper':
        print(" u loose :(.")
        count2=+1
    elif userChoice == 'paper' and pythonChoice == 'paper':
        print('nobody wins its a tie :o')
    


print("now results time :)")
print(f"your score {count} and python score {count2} ") 
if count2 > count:
    print("PYTHON WON ")
elif count2 < count:
    print("u won the game CONGRATS BUDDY :).")
else:
    print("the game is tied u both played well.")

