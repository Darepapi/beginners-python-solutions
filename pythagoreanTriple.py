#A check for pythagorean triple
user_choice = input("Do you want to check if some numbers are pythagorean triple? yes/no  ")
while user_choice == "yes":
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    num3 = int(input("Please enter the third number: "))
    if (num1**2 + num2**2) == num3**2:
        print("The number is a Pythagorean Triple!!")
    else:
        print("The number is not a Pythagorean triple!")
    user_choice = input("Do you want to check if some numbers are pythagorean triple? yes/no  ")
