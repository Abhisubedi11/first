print("basic calculator")
number1 = float(input("enter first number:"))
number2 = float(input("enter second number:"))
print("press 1 for add \n2 for subtraction \n3 for multiplication \n 4 for division")

choice = int(input("enter youre choice from 1 to 4:"))

if choice == 1:
print ("the sum is:", number1 + number2)
elif choice == 2:
print("the subtraction is:", number1 - number2)
elif choice == 3:
print("the multiplication is:", number1 * number2 )
elif choice == 4:
print("the division is:", number1 / number2)
else :
print("INvalid input")

