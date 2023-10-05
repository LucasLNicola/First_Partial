#Sum and Rest

def sum(a,b):
  x = a + b
  return x

def rest(a,b):
  x = a - b
  return x

print("Give me the first number")
a = int(input())
print()
print("Give me the second number")
b = int(input())
print()
print("The sum is", sum(a,b), "and the rest is", rest(a,b))
print()
#------------------------------
#Guided Round
#Multiplication and Division

def multiplication(a,b):
  x = a * b
  return x

def division(a,b):
  x = a/b
  return x

print("Give me the first number")
a = int(input())
print()
print("Give me the second number")
b = int(input())
print()
print("The multiplication is", multiplication(a,b), "and the division is", division(a,b))
print()
#----------------------------
#Unit Conversion

def convertor(km):
  m = km * 1000
  return m

print("How many kilometers have passed so far? ")
km = int(input())
print()
print("So far you have passed", convertor(km), "meters")
print()
#-------------------------
#

def triangle_area():
  a = (b*h)/2
  return a

print("What't the base of your triangle?")
b = float(input())
print()
print("What's your height?")
h = float(input())
print()
print("The area of your triangle is", triangle_area())

#------------------------------
#
