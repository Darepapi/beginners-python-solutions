def lyrics(n):
    while n != 1:
        if n < 1:
            break
        else:
            print()
            if n > 1:
                print(n,'bottles of beer on the wall \n'+str(n)+' bottles of beer')
                print('Take one down, pass it around')
                n -= 1
                if n == 1:
                    print(str(n)+' bottle of beer on the wall')
                else:
                    print(str(n)+' bottles of beer on the wall')
lyrics(99)