# Python program to check if year is a leap year or no
# To get year (integer input) from the user
year = int(input("Enter a year: "))
if(year%4==0 and year%100!=0) or (year%4==0 and year%100==0 and year%400==0):
  print(year," is a leap year")
else:
    print(year," is not a leap year")
  