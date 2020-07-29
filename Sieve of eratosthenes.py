"Sieve of eratosthenes: It is a algorithm to find all the prime number i given range"

from math import *

def sieve(n):
    prime=[True]*(n+1)
    prime[0]=False
    prime[1]=False
    for p in range(2, int(sqrt(n)+1)):
        if prime[p]==True:
            for i in range(p*p, n+1, p):
                prime[i]=False
    for i in range(0,len(prime)):
        if prime[i]==True:
            print(i, end=" ")


n=int(input("Enter Number to which you want prime numbers:\n"))
print(sieve(n))
