'''
@Author: Shruti
@Date: 2021-12-30
@Last Modified by: Shruti
@Last Modified time: 2021-12-30 
@Title : Power o 2 using command line arguments
'''

import sys

Y = int(sys.argv[1])

if 0<Y<32:
    x=[2**i for i in range(Y+1)]
    print(x)
else : 
    print("Invalid Number")