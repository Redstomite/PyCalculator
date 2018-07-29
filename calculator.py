#Rahul Pycalc v0.3
class Calculator():

	name = None

	def __init__(self, name):
		self.name = name

	def add(self, a , b):
		addresult = a+b	
		return(addresult)

	def sub(self, a , b):
		return(a-b)

	def times(self, a , b):
		return(a*b)

	def div(self, a , b):
		return(a/b)

class Scicalculator(Calculator):

	def power(self, a , b):
		return (a**b)

	def sqrroot(self, a):
		return(a**(0.5))

	def fracper(self, a , b):
		return(a/b*100)
		


obj1 = Scicalculator("Pycalc")
print("Welcome to pycalc v0.3")
sci = input("Do you want to do exponentation, squareroot or conversion(frac{1/2} --> per{%})? y/n  ")
if sci == "y":
	c = input(("Type e / s / c for your function  "))
	results = "empty"	
	if c == "e":	
		a = float(input("Name your number  "))
		b = float(input("Name your power  "))
		results = obj1.power(a, b)
	elif c == "s":
		a = float(input("Enter your number for Square root."))
		results = obj1.sqrroot(a)
	
	elif c == "c":
		a = float(input("Enter your Numerator  "))
		b = float(input("Enter your Denominator  "))
		results = obj1.fracper(a,b)
	print(results)

elif sci == "n":
	c = input("What do you want to do?(+ , - , / , *,)  ")
	a = float(input("What is the first number?  "))
	b = float(input("What is the second number?  "))
	results = "empty1"
	if c == "+":
		results = obj1.add(a,b)
	elif c == "-":
		results = obj1.sub(a,b)
	elif c == "/":
		results = obj1.div(a,b)
	elif c == "*":
		results = obj1.times(a,b)
	else:
		results = "Invalid"

	print(results)


