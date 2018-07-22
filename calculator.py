print("Welcome to pycalc v0.1")
print("My name is pybot")
name=str(input("What is your name?"))
print("Hello,",name)
c = input("What do you want to do?",name,"	")
a = int(input("Enter The first number	"))
b = int(input("Enter the second number	"))
if c == "+":
	print("The answer is:",a+b)
elif c == "-":
	print("The answer is:",a-b)
print("We will add division and multiplication in version 0.2")
