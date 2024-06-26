#python

#taking user data and storing it in a variable.
a=int(input("enter a number"))

#taking another number from user and storing it in b.
b=int(input("enter another number"))

#trying a/b and if there is an error in this statement then it will run the ecept statement.
try:
  print(a/b)
except:
  print("value of b is zero")
