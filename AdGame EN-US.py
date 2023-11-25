# Imports, value definitions, and variable declarations section

import random, time, emoji

AttemptsCounter = 0

while True:
    MachineChoice = random.randrange(0, 6)
    print('\n\033[1;33mWelcome! \033[0;0mthis python file is a guessing game made by \033[1;36mG.Felix!\033[0;0m\n')
    time.sleep(3.5)

    # Part 2: Input definition and adjustments for possible errors

    while True:
        print('\033[H\033[J')
        UserGuess = input('~-' * 58 + '\n\n\033[1;31mLet`s get started with the game!\033[0;0m\n\nChoose \033[1;31mone\033[0;0m of the options below for your guess and try to guess the number i`m thinking of...\n\n\033[1;36m[0]\033[0;0m \033[1;35m[1]\033[0;0m \033[1;34m[2]\033[0;0m \033[1;33m[3]\033[0;0m \033[1;32m[4]\033[0;0m \033[1;30m[5]\033[0;0m\n\n' + '~-' * 58 + '\n\n\033[1;32m---> \033[0;0m').strip()

        if UserGuess.isnumeric() and int(UserGuess) in range(6):
            break

        else:
            time.sleep(2)
            print('\n\033[1;33mSomething went wrong. Checking...\033[0;0m')
            time.sleep(2)
            print('\n\033[1;31mInvalid input\033[0;0m! Enter only numbers between \033[1;31m0\033[0;0m and \033[1;31m5.\033[0;0m')
            time.sleep(2.8)

            # Clear the console after the message error
            print('\033[H\033[J')

    # Results part (3)
    print(emoji.emojize('\n\033[1;33mLet`s see if your guess is correct...\033[0;0m :thinking_face:\n'))

    time.sleep(2)

    if int(UserGuess) != MachineChoice:
        AttemptsCounter += 1

    if int(UserGuess) == MachineChoice:
        print(emoji.emojize('\033[1;32mWoow... First-rate\033[0m!!! :face_with_peeking_eye:'))
        print(emoji.emojize('\nYou \033[1;32mgot it\033[0;0m!! You got me this time... :person_shrugging:'))
        time.sleep(5.2)
        print('\033[H\033[J')

    # Below here, it will show that the user got it wrong and ask for their input again, thereby counting with the variable 'AttemptsCounter', while the user does not meet the requirement of the while loop, the program will keep asking for a new guess and counting how many times they get it wrong.
    else:
        time.sleep(0.9)
        print(emoji.emojize('\033[1;31mIt seems like someone made a mistake hahaha, try again! :confused_face:'))
        while MachineChoice != UserGuess:
            UserGuess = input('\n\033[1;35mWhat`s your new guess?\033[1;35m\n---> \033[1;32m')


            # If the input meets the requirements of the while loop, the next checks will occur below.
            if UserGuess.isnumeric() and int(UserGuess) in range(6):
                pass

            # If the input does not meet the requirements of the if statement above, it will fall into this else statement and the following error message will be displayed, asking the user to enter a valid number again.
            else:
                time.sleep(1.2)
                print('\n\033[1;31mInvalid input\033[0;0m! Enter only numbers between \033[1;31m0\033[0;0m and \033[1;31m5.\033[0;0m')
                time.sleep(1.1)
                continue

            # Checking if the player's guess is greater than, less than, or equal to the computer's chosen number.
            if MachineChoice > int(UserGuess):
                time.sleep(0.7)
                print(emoji.emojize('\n\033[1;33mMore... :smirking_face: Try your guess again\033[0m'))
                AttemptsCounter += 1

            if MachineChoice < int(UserGuess):
                time.sleep(0.7)
                print(emoji.emojize('\n\033[1;34mLess... :sad_but_relieved_face: Try your guess again\033[0m'))
                AttemptsCounter += 1
                
            # Here the success message will be displayed, and outside of this loop we will be shown the number of attempts that were used to arrive at the final result.
            if int(UserGuess) == MachineChoice:
                print(emoji.emojize('\nYou \033[1;32mgot it\033[0;0m!! Ah, haha... You got me this time :face_holding_back_tears:'))
                AttemptsCounter += 1
                break

        # Displaying the attempts along with the console clear.
        time.sleep(2)
        print(f'\n\033[1;34mYou took \033[43;1;30m{AttemptsCounter}\033[0;0m \033[1;34mattempts to guess the chosen number.\033[0m')
        time.sleep(4)
    print('\033[H\033[J')

    # In this part, I want to ask the user if they want to play again to make it an interesting game to play.
    PlayAgain = input('\nPlay \033[1;32magain\033[0;0m? (Y/N): ').lower().strip()

    # Validation of input response 'PlayAgain'
    while PlayAgain not in ['y', 'n']:
        PlayAgain = input('\n\033[1;31mInvalid option\033[0;0m. Play again? (Y/N): ').lower().strip()
        continue

    # To check the user's response for the first or second input in case they entered it incorrectly and execute the following commands, whether it is 'continue' or 'break'.
    if PlayAgain == 'y':
        AttemptsCounter = 0
        print('\033[H\033[J')
        continue

    if PlayAgain == 'n':
        break