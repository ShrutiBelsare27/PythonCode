'''
@Author: Shruti
@Date: 2021-12-30
@Last Modified by: Shruti
@Last Modified time: 2021-12-30 
@Title : Print the harmonic value
'''

sum=0
n=int(input("Enter a number "))
if n!=0:
    i=1
    for i in range(1,n+1):
        sum=sum+(1/i) # harmonic sum calculation
        print("value of 1/i"," is ",  1/i)
    print("Harmonic sum is",sum)
else:
    print("Number should not equal to zero")