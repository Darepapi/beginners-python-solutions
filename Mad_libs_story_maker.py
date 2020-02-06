import sys

username = input('Please enter your username: ').capitalize()
print(f'\nWelcome {username}!')
user_prompt = input('Do you wish to play Mad Libs word game?  (yes/no)  ')

#loop to make sure user enter either yes or no 
while user_prompt.capitalize() != 'Yes' or user_prompt.capitalize() != 'No':
    
    if user_prompt.capitalize() == 'Yes':
        print('\n                          >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Question <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
       
       
        print("""\n                    -----------------------------------------------------------------------------------------------------------------------------------------------------
                    :           My friend asked me to____________________ five _______________________federal university in Nigeria,                                    :
                    :                                        (verb 1)                  (adjective 1)                                                                    :
                    :                                                                                                                                                   :
                    :              I ___________________  UI, UNILAG, UNIBEN, UNILORIN  ________________________    _________________________.                          :
                    :                    (verb 2)                                      (conjuction 1)                      (Noun 1)                                     :
                    :                                                                                                                                                   :
                    :            _______________  _______________  asked me why i  _____________________________ mention __________________________.                    :
                    :              (Pronoun 1)      (adverb 1)                         (negative verb )                            (noun 2)                             :
                    :                                                                                                                                                   :
                    :        Please _______________, if you are ask to mention the ______________________ you know, Will you _______________    _____________________?  :
                    :                   (noun 3)                                      (Celestial Noun 1)                        (verb 3)          (Celestial Noun 2)    :
                    -----------------------------------------------------------------------------------------------------------------------------------------------------
            """)


        print('                       >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Loading Frameworks...... <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

        verb1 = input('\nEnter \'Verb 1\': ')
        adjective1 = input('Enter \'Adjective 1\': ')
        verb2 = input('Enter \'Verb 2\': ')
        conjuction1 = input('Enter \'Conjunction 1\': ')
        noun1 = input('Enter \'Noun 1\': ').upper()                                  #convert noun 1 string to uppercase
        pronoun1 = input('Enter \'Pronoun 1\': ')
        adverb1 = input('Enter \'Adverb 1\': ')
        negative_verb = input('Enter \'Negative Verb\': ')
        noun2 = input('Enter \'Noun 2\': ').upper()                                  #convert noun 1 string to uppercase
        noun3 = input('Enter \'Noun 3\': ').capitalize()
        Celestial_noun1 = input('Enter \'Celestial Noun 1\': ').capitalize()         #convert first letter of the word to uppercase
        verb3 = input('Enter \'Verb 3\': ')
        Celestial_noun2 = input('Enter \'Celestial Noun 2\': ').capitalize()         #convert first letter of the word to uppercase


        print('                     >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Compiling story..  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')


        print(f"""  
                                                        Your bullshit story!
                    ---------------------------------------------------------------------------------------------------------------------------
                        My friend asked me to {verb1} five {adjective1} federal university in Nigeria,                                       
                        I {verb2} UI, UNILAG, UNIBEN, UNILORIN {conjuction1} {noun1} .                                                        
                        {pronoun1} {adverb1} asked me why i {negative_verb} mention {noun2} .                                                 
                        Please {noun3}, if you are ask to mention the {Celestial_noun1} you know, Will you {verb3} {Celestial_noun2}?         
                                                                                                                                           
                    ---------------------------------------------------------------------------------------------------------------------------
                """)
    elif user_prompt.capitalize() == 'No':
        print('Get the fuck outta here! ')
        sys.exit()