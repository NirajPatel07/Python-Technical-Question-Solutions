"""Check Prime"""

#Naive Method (Inefficient)

def prime1(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c>2:
        return False
    return True

# Efficient Method

def prime2(n):
    if n==0 or n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0 or n%5==0 or n%7==0:
        return False
    return True

n=int(input("Enter Number:\n"))
print("Naive method:\n",prime1(n))
print("Efficient Method:\n",prime2(n))
