from random import *
import sys

list1 = ['Scissors', 'Paper', 'Rock']


while True:
    user_prompt = input('Do you wish to play RPS?   yes/no: ')
    if user_prompt == 'yes':
        print('Welcome on board! ')
        if user_prompt == 'yes':
            computer_turn  = choice(list1)
            user_turn = input('Rock? Paper? or Scissors?  ')
            if user_turn.capitalize() == 'Rock':
                if computer_turn == 'Paper':
                    print('Computer wins! As Computer choice is',computer_turn,'and your choice is',user_turn,'!!!\nReason.\nAs Paper will always cover Rock.')
                elif computer_turn == 'Scissors':
                    print('You win! As Computer choice is',computer_turn,'and your choice is',user_turn,'!!!\nReason.\nAs Rock will always crush Scissors.')            
            elif user_turn.capitalize() == 'Paper':
                if computer_turn == 'Rock':
                    print('You win! As Computer choice is',computer_turn,'and your choice is',user_turn,'!!!\nReason.\nAs Paper will always cover Rock.')
                elif computer_turn == 'Scissors':
                    print('Computer wins! As Computer choice is',computer_turn,'and your choice is',user_turn,'!!!\nReason.\nAs Scissors will always cut Paper.')
            elif user_turn.capitalize() == 'Scissors':
                if computer_turn == 'Rock':
                    print('Computer wins! As Computer choice is',computer_turn,'and your choice is',user_turn,'!!!\nReason.\nAs Rock  will always crush Scissors.')
                elif computer_turn == 'Paper':
                    print('You win! As Computer choice is',computer_turn,'and your choice is',user_turn,'!!!\nReason.\nAs Scissors will always cut Paper.')
            elif user_turn.capitalize() == computer_turn:
                print('You just picked the same choice with the computer!!')
    elif user_prompt == 'no':
        print('Goodbye!')
        sys.exit()
    else:
        print('Please enter a correct value! ')