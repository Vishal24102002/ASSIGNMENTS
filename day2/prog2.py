#PYTHON 

#initial array 
array=[1,2,3]
#user input in array
uservar=input("enter the multiple values with comma in them")

#converting user input to list 
uservar=uservar.split(",")

#looping for the numbers present in uservar
for i in uservar:
    array.append(int(i))

#displaying the result
print(array) 