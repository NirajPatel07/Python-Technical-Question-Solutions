#Sum of N numbers.


# Naive Method (Inefficient) Time Complexity O(n)
def sumOfN1(n):
    s=0
    for i in range(n+1):
        s+=i
    return s


#Efficient Method, Time Complexity O(1)

def sumOfN2(n):
    return (n*(n+1))//2

n=int(input("Enter number:\n"))
print(sumOfN1(n))
print(sumOfN2(n))
