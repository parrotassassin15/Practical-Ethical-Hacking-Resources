#!/usr/bin/env python3

# Variables and modules
quote = "All is fair in love and war"
print(quote.upper()) # uppercase
print(quote.lower()) # lowercase
print(quote.title()) # title

print(len(quote)) # gets length of quote

name = "Heath" # string
age = 30 # int
gpa = 3.7 # float

print(int(age)) # casting int as int
print(int(30.9)) # casting float as int

print("Hello, my name is " + name + " and I am " + str(age) " years old!")

age+=1
print(age)

birthday = 1
age += birthday
print(age)

print('\n')

#Functions
print("This is an example of a function")

def who_am_i():
  name = "Heath"
  age = 30
  print("My name is " + name + " and I am " + str(age) + " years old!")
  
who_am_i()

# adding params
def add_one_hundred(num):
  print(num + 100)

add_one_hundred(100)

# multiple params
def add(x,y):
  print(x + y)
  
add(7,7)

def multiply(x,y):
  print(x * y)
  
multiply(7,7)

def square_root(x):
  print(x ** 0.5)
  
square_root(25)

def nl():
  print('\n')
  
nl()

# boolean expressions (true/false)
print("Boolean Expressions:")
bool1 = true
bool2 = 3 * 3 ==9
bool3 = false
bool4 = 3 * 3 !=9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

nl()

# Relational and boolean expressions

greater_than = 7 > 5
less _than =  5 < 7
greater_than_equal_to = 7 >= 7 
less_than _ equal_to = 7 <= 7

test_and1 = (7 > 5) and (5 < 7) # true
test_and2 = (7 > 5) and (7 > 5) # false
test_or =  (7 > 5) or (5 < 7) # true
test_or2 = (7 > 5) or (5 > 7) # false

test_not = not true #false

nl()
#Conditional statements
def drink(money):
  if money >= 2:
    return "You've got yourself a drink"
  else:
    return "yeah, NO. get outta here"

drink(2)
drink(1)

def alcohol(age,money):
  if (age >= 21) and (money >= 5):
    return "Lucky you, it's happy hour!"
  elif (age >= 21 ) and (money < 5):
    return "not enought bud"
  elif (age < 21) and (money >= 5):
    return "Nice try kid"
  else
    return "You're broke and too young"
  
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))
  
nl()
# lists []
movies = ["Hangover", "The Perkins", "Spiderman 3"]
  
print(movies[1]) # return second item
print(movies[0]) # returns first item
print(movues[1:4])
print(movies[1:])
print(movies[:2])
print(movies[-1]) 

print(len(movies))
movies.append("JAWS")
print(movies)

movies.pop()
print(movies)

movies.pop(0)
print(movies)

nl()
#Tuples - static, ()
grades = ("a", "b", "c", "d", "f")
print(grades[1])

nl()
# Loops
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
    print(x)
    
 # While loops - execute so long as true

i = 1

while i < 100:
  print(i)
  i+=1
  
  
