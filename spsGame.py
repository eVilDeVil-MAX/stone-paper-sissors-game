import random

component = ['rock', 'paper', 'scissors']
user_wins = 0
python_wins = 0
draw_count = 0
win_text = ['You win!',
            "hey guess what , you won :). ",
            'yee, u won ',
            ]
lose_text = ['You lose!',
             "congrats computer wins this time :(.",
             "oh no python won this time :(",
             'shoot python won ',
             " u loose :(."
             ]
draw_text = ['Draw!',
             'its a tie 0.0',
             "its a tie.",
             'its a tie nobody loses.',
             'nobody wins its a tie :o'
             ]

games = int(input('How many game you wanna play? '))
print()
for i in range(games):
    print(f"these are ur options ({', '.join(component)})")
    userChoice = input("enter what you choice: ")
    pythonChoice = random.choice(component)
    print(f"python chose: {pythonChoice}")

    if userChoice == 'rock':
        if pythonChoice == 'scissors':
            print(random.choice(win_text))
            user_wins +=1
        if pythonChoice == 'paper':
            print(random.choice(lose_text))
            python_wins +=1

    if userChoice == 'paper':
        if pythonChoice == 'rock':
            print(random.choice(win_text))
            user_wins += 1
        if pythonChoice == 'scissors':
            print(random.choice(lose_text))
            python_wins += 1

    if userChoice == 'scissors':
        if pythonChoice == 'paper':
            print(random.choice(win_text))
            user_wins += 1
        if pythonChoice == 'rock':
            print(random.choice(lose_text))
            python_wins += 1

    if userChoice == pythonChoice:
        print('Draw!')
        draw_count +=1
    print()


print("now results time :)")
print(f"your score {user_wins}")
print(f"python score {python_wins}")
print(f"draws {draw_count}")
