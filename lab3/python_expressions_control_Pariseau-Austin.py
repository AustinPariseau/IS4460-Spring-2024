##boolean

print(f"is 6 greater than 7? {6 > 7}")
print(f"is 1 less than 125? {1 < 125}")
print(f"is 483882 equal to 10000? {483882 == 10000}")
print(f"is 0 equal to 0? {0 == 0}")

##boolean as int


print("nine is eqal to nine:" ,int(9==9))
print("seven is less than four:" ,int(7<4))

##literals and variables


myname = "The senate"
myage = "75"

print(f"a: {65}")
print(f"b: {'You underestimate my power'}")
print(f"c: {False}")
print(f"c: {myname}")
print(f"e: {myage}")

##precedence

print((3-1+39),(47-12+3))
print((3*65+3),(43*2+5))


##relational operators

print(f"is 'sus' == 'suspense'? {'sus' == 'suspense'}")

##equality operators


my_name= "captain"
print("Rank: ", my_name)
print("Current Position: ", my_name == "captain")

##comparison operators

print("comparison:","zz" < "zzzzzzz")
print("comparison:",1000 < 1)

##if else elif

bank_balance = -32
lottery_winnings = 1000000
if bank_balance <= 0:
  print("you broke man")
elif bank_balance < 100:
  print("you gotta keep working man")
else:
  print("you did good, heres a winning lottery ticket")
  bank_balance + lottery_winnings



##ternary operator

jet_fuel = 5200
print("Full tank" if jet_fuel == 5200 else "Tank not full")