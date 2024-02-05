##comments

# This comment is mine, I love my comment

##literals

print('Han Solo') #He made the Kessel run in less than 12 parsecs, also this is a string
print(12.1) #this is a special number called a float

##variable names


z = 42
Z = 24

print(z)
print(Z)

##This criterion is linked to a Learning Outcomestrings and variables + and f string

user_name = "Din Djarin"
gpa = 2.1

print(user_name)
print(gpa)

print("My name is " + user_name + ", you killed my family, prepare to die")
print(f"My name is {user_name}, you killed my family, prepare to die")

##converting between types and substring

number = 82818 * 3991919939
print(str(number)[0:3]) #to get the first 3 numbers you actually need to start at index location 0 because that would be the first number

##a,b function

def add_numbers(a,b):
  output = (a/b)
  return output
  

print(add_numbers(5,2)) #positional
print(add_numbers(b = 100, a = 382881)) #name

##say_hello function

name = "Jar Jar"

def say_hello():
  name = "Boss Nass"
  return f"Hello {name}"

print(say_hello())