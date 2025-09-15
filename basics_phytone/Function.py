#Creating a Function
def my_function():
  print("Hello from a function")
#Calling a Function
my_function()
#Function Arguments
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
#Function with Multiple Arguments
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")
my_function("Tobias", "Refsnes")
#Keyword Arguments
def my_function(fname, lname):
  print(fname + " " + lname)
my_function(lname="Refsnes", fname="Emil")
my_function(lname="Refsnes", fname="Tobias")
#Default Parameter Values
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
# Arbitrary Arguments, *args
def my_function(*kids): #the asterisk (*) before the parameter name *kids
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
# Arbitrary Keyword Arguments, **kwargs
def my_function(**kid): #kwargs stands for keyword arguments
  print("His last name is " + kid["lname"])
my_function(fname="Emil", lname="Refsnes")
#Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)
my_function(["apple", "banana", "cherry"])
#Return Values
def my_function(x):
  return 5 * x 
print(my_function(3))
# The pass Statement
def myfunction():
  pass #will do nothing
#myfunction() #no error
#Positional-Only Arguments
def my_function(pos1, pos2, /, pos3):
  print(pos1, pos2, pos3)
my_function(1, 2, 3) #correct
#my_function(1, pos2=2, pos3=3) #wrong
my_function(1, 2, pos3=3) #correct
#Keyword-Only Arguments
def my_function(pos1, pos2, /, *, kw1, kw2):
  print(pos1, pos2, kw1, kw2)
my_function(1, 2, kw1=3, kw2=4) #correct
#my_function(1, pos2=2, kw1=3, kw2=4) #wrong
#my_function(1, 2, 3, kw2=4) #wrong
my_function(1, 2, kw1=3, kw2=4) #correct
#Function Annotations
def my_function(x: int, y: int) -> int:
  return x + y
print(my_function(5, 6))
print(my_function("5", "6"))