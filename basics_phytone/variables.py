#declare variables
x = 10
y = "yassine"
print(x)
print(y)
print("hello " + y)
print(type(x))

#Casting
z = float(x)
x = str(x)
y = int(z)
print(z)
print("The type of z is: " + str(type(z)))
print("The type of x is: " + str(type(x)))
print("The type of y is: " + str(type(y)))

#Legal variable names
myvar = "yassine"
my_var = "yassine"
_my_var = "yassine"
myVar = "yassine"
MYVAR = "yassine"
myvar2 = "yassine"
#Illegal variable names
#2myvar = "yassine"
#my-var = "yassine"
#my var = "yassine"
#my.var = "yassine"
#my@var = "yassine"
#my%var = "yassine"
#my#var = "yassine"
#my^var = "yassine"
#my&var = "yassine"
#my*var = "yassine"
#my(var) = "yassine"
#my+var = "yassine"
#my=var = "yassine"
#my{var} = "yassine"
#my[var] = "yassine"
#my;var = "yassine"
#my:var = "yassine"
#my,var = "yassine"
#my<var> = "yassine"
#my.var = "yassine"
#my?var = "yassine" #etc...

#Many Values to Multiple Variables
a, b, c = "orange", "banana", "cherry"
print(a)
print(b)
print(c)
#One Value to Multiple Variables
d = e = f = "yassine"
print(d)
#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
g, h, i = fruits
print(g)
print(h)    
print(i)

#Output Variables
print(g + h + i)
print(g + " " + h + " " + i)
print(g, h, i)
"""
In the print() function, when you try to combine a 
string and a number with the + operator, Python will give you an error:
"""
# Global Variables
glob_var = "I am global"
make_local = "I am global too"
# Local Variables
def myfunc():
    print("This is a function")
    print("I can access global variable: " + glob_var)
    local_var = "I am local"
    print("I am a local variable: " + local_var)
    make_local = "I am local"
    print("I can access global variable too: " + make_local)

myfunc()
print("I can access global variable outside function: " + glob_var)
print("I can access global variable too outside function: " + make_local)

#example of local variable error
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x) #Python is fantastic

myfunc()

print("Python is " + x) #Python is awesome

# global keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) #Python is fantastic
# global keyword to change a global variable inside a function
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) #Python is fantastic