#Rahul Pycalc v0.2.1
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

obj1 = Scicalculator("Pycalc")
print("Welcome to pycalc v0.2.1")
sci = input("Do you want to do power? y/n  ")
if sci == "y":
	a = float(input("Name your number  "))
	b = float(input("Name your power  "))
	results = obj1.power(a, b)

elif sci == "n":
	a = float(input("What is the first number?  "))
	b = float(input("What is the second number?  "))
	c = input("What do you want to do?(+ , - , / , *, **)  ")
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

