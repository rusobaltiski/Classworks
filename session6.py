print(5 or 7)
print(5 and 7)
print(None or False or 11 or 12 or 0)
print(7 and 8 and 0 and 9 and False and 10)
print(7 and 8 and 9 and 10)

print("2<5=", 2 < 5)
print("2==2.0 is", 2 == 2.0)

a = 5  #assignment, a takes the value of 5
a = a + 1
print(a)
a *= 3
print(a)
a /= 7
print(a)

name=input("what is your name? ")
print("nice to meet you", name)
age=input("what is your age?")


try:
    age=int(age)
    print("you were born in", 2026-age)
except ValueError :
  print("that is not a proper answer")
  print("don´t be smart with me")
except NameError :
  print("that is not a proper answer")
except:
    print("this will catch all other exceptions")
else:
    print("thanks for playing fair")
finally:
    print("this will be done no matter what")
