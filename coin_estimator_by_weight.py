import math

print('Welcome to the Official Coin Estimator! ')
print('-------------------------------------------')

#Using the loop to make sure user enter either 'grams' or 'pounds'
weightType =    input('Would you like to submit your coin weight in Grams or Pounds? ')
while weightType != 'pounds' and weightType != 'grams':
    print('You entered a wrong value!')
    weightType = input("Please enter either 'Grams' or 'Pounds': ")

#prompt to accept user coin weight
coinPennies =   math.ceil(float(input('Enter the Total weight of Pennies: ')))
coinNickels =   math.ceil(float(input('Enter the Total weight of Nickels: ')))
coinQuarters =  math.ceil(float(input('Enter the Total weight of Quarters: ')))
coinDimes =     math.ceil(float(input('Enter the Total weight of Dimes: ')))

#conversion of pounds to gram if weight type is pound >>>>> 1pounds == approximately 454grams <<<<<<<<
if weightType == 'pounds':
    coinPennies = coinPennies * 454
    coinDimes = coinDimes * 454
    coinQuarters = coinQuarters * 454
    coinNickels = coinNickels * 454
else:
    pass

def coin_wrapper(penny, Nickels, Dimes, Quarters):
    #initiate cash worth for coins to avoid UnboundLocalError
    cash_worth_for_dime = 0
    cash_worth_for_nickel = 0
    cash_worth_for_quarters = 0
    cash_worth_of_penny = 0

    """ Calculation for the amount of  Coin wrapper needed for Penny. 1 penny == 2.5g, one wrapper of penny == 50 pennies with a worth of $0.50  """
    if penny:
        print('\n----------Penny details----------')
        amount_of_penny = math.ceil(penny/2.5)
        number_of_wrapper_needed = math.ceil(amount_of_penny/50)
        if amount_of_penny < 50:
            remain_penny = 50-amount_of_penny
            print(f'You currently have {amount_of_penny} pennies!\nYou need additional {remain_penny} pennies to fill up a Coin Wrap.')
        else:
            #estimate the dollar worth of the coin wrapper.
            cash_worth_of_penny = math.ceil(0.50 * number_of_wrapper_needed)
            print(f'You currently have {amount_of_penny} pennies!\nYou will need {number_of_wrapper_needed} coin wraps which worths ${cash_worth_of_penny}!')

    """ Calculation for the amount of  Coin wrapper needed for Nickel. 1 nickel == 5g, one wrapper of Nickel == 40 nickels with a worth of $2.0  """
    if Nickels:
        print('\n----------Nickel details----------')
        amount_of_nickel = math.ceil(Nickels/2.5)
        number_of_wrapper_needed_for_nickel = math.ceil(amount_of_nickel/50)
        if amount_of_nickel < 40:
            remain_nickel = 40-amount_of_nickel
            print(f'You currently have {amount_of_nickel} Nickels!\nYou need additional {remain_nickel} nickels to fill up a Coin Wrap.')
        else:
            #estimate the dollar worth of the coin wrapper.
            cash_worth_for_nickel = math.ceil(2 * number_of_wrapper_needed_for_nickel)
            print(f'You currently have {amount_of_nickel} nickels!\nYou will need {number_of_wrapper_needed_for_nickel} coin wraps which worths ${cash_worth_for_nickel}!')
    
    """ Calculation for the amount of  Coin wrapper needed for dime. 1 dime == 2.268g, one wrapper of Dime == 50 dimes with a worth of $5.0"""
    if Dimes:
        print('\n----------Dime details----------')
        amount_of_dime = math.ceil(Dimes/2.5)
        number_of_wrapper_needed_for_dime = math.ceil(amount_of_dime/50)
        if amount_of_dime < 50:
            remain_dime = 50-amount_of_dime
            print(f'You currently have {amount_of_dime} dimes!\nYou need additional {remain_dime} dimes to fill up a Coin Wrap.')
        else:
            #estimate the dollar worth of the coin wrapper.
            cash_worth_for_dime = math.ceil(5 * number_of_wrapper_needed_for_dime)
            print(f'You currently have {amount_of_dime} dimes!\nYou will need {number_of_wrapper_needed_for_dime} coin wraps which worths ${cash_worth_for_dime}!')
    
    """ Calculation for the amount of  Coin wrapper needed for quarters. 1 quarter == 5.67g, one wrapper of quarter == 40 quarters with a worth $10.0  """
    if Quarters:
        print('\n----------Quarters details----------')
        amount_of_quarters = math.ceil(Quarters/2.5)
        number_of_wrapper_needed_for_quarters = math.ceil(amount_of_quarters/50)
        if amount_of_quarters < 40:
            remain_quarters = 40 - amount_of_quarters
            print(f'You currently have {amount_of_quarters} Nickels!\nYou need additional {remain_quarters} nickels to fill up a Coin Wrap.')
        else:
            #estimate the dollar worth of the coin wrapper.
            cash_worth_for_quarters = math.ceil(10 * number_of_wrapper_needed_for_quarters)
            print(f'You currently have {amount_of_quarters} nickels!\nYou will need {number_of_wrapper_needed_for_quarters} coin wraps which worths ${cash_worth_for_quarters}!')
    total_amount = math.ceil(cash_worth_for_dime + cash_worth_for_nickel + cash_worth_for_quarters + cash_worth_of_penny)
    print(f'\n ----------The Estimated amount for your coins is ${total_amount}----------')

coin_wrapper(coinPennies, coinNickels, coinDimes, coinQuarters)

