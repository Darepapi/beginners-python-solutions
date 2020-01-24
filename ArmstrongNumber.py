def armstrong_num():
    while True:
        numlen = input('Please enter a number to check if it is an Armstrong Number or enter "0" to quit: ')
        if int(numlen) == 0:
            break
        else:
            n = len(numlen)
            total = 0
            for num in numlen:
                total = total + int(num)**n
            if int(numlen) == total:
                print('The Value you entered is an Armstrong Number! ')
            else:
                print('The Value is not an Armstrong number!')
armstrong_num()
print('Goodbye!')