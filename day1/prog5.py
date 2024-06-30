#python 

year=int(input("enter the year to check :"))

if (year%4==0 and year%100!=0) or (year%400==0):
  print(f"yes {year} is a leap year")
else:
  print(f"no {year} is not a leap year")
