# Print this pyramid pattern.
'''
n=3
  *
 *** 
*****
'''

'''
n=5
    *
   ***
  *****
 *******
********* spaces=4,3,2,1,0= n-i      and stars=1,3,5,7,9= 2*i-1
'''

n=int(input("enter your number: "))

for i in range(1,(n+1)):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("\n")

