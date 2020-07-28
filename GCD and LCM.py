""" Find Gcd and Lcm"""

#Efficient Method

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def lcm(a,b):
    prod=a*b
    hcf=gcd(a,b)
    lcm=prod/hcf
    return int(lcm)

a=int(input("Enter a:\n"))
b=int(input("Enter b:\n"))
print(gcd(a,b))
print(lcm(a,b))
