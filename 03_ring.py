# Pattern ring
'''
n=3
***
* *
***
n=4
****    star=4
*  *    1"*",2" ",1"*"
*  *    1"*",2" ",1"*"
****    star=4
'''

n=int(input("enter your number: "))

for i in range(1,(n+1)):
    if(i==1 or i==n):
        print("*"*n,end="")
        print("\n")
    

    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
        print("\n")
print("done")