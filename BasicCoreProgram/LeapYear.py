'''
@Author: Shruti
@Date: 2021-12-30
@Last Modified by: shruti
@Last Modified time: 2022-1-2
@Title : To check whether entered year is a leap year or not
'''

year=int(input("Enter the year: "))
count=0
if count==4:
    if year % 4==0:
        if year % 100==0:
            if year % 400==0:
                print(year,"is a leap year")
            else:
                print(year,"is not a leap year")
        else:
             print(year,"is a leap year")    
        
    else:
        print(year,"Not a leap year")  
else:
      print("year is not 4 digit")        