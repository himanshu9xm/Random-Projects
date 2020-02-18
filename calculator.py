def sum(x , y):
	return x + y
def sub(x , y):
    return x - y
def mul(x , y):
	return x * y
def div(x , y):
	return x / y

print("Enter the choice 1.Add 2.Subtract 3.Muntiply 4. Divide")
print("Select a option 1/2/3/4")
choice = input()
num1 = int(input("Enter first no."))
num2 = int(input("Enter second no."))
if choice == '1':
	print(num1, "+", num2, "=", sum(num1, num2))
elif choice == '2':
	print(num1, "-", num2, "=", sub(num1, num2))
elif choice == '3':
	print(num1, "*", num2, "=", mul(num1, num2))
elif choice == '4':
	print(num1, "/", num2, "=", div(num1, num2))
else : 
	print("Invalid Input")
	