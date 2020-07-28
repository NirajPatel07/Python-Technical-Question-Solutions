"""Find all the divisior of a number"""

from math import *

# Naive Method

def div1(n):
    ans=[]
    for i in range(1,n+1):
        if n%i==0:
            ans.append(i)
    return ans

# Efficient Method

def div2(n):
    ans=set()
    for i in range(1, int(sqrt(n))):
        if n%i==0:
            ans.add(i)
            ans.add(int(n/i))
    return list(ans)
    
        


n=int(input("Enter Number:\n"))
print(div1(n))
print(div2(n))
