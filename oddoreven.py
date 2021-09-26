def addition(num, num2):
    return int(num) + int(num2)


num = input("enter number 1:")
num2 = input("enter number 2:")
total = addition(num,num2)

if(total%2):
	print(total)
	print("your number is odd")
else:
	print(total)
	print("your number is even")