# Project : Prime-check + Factorial
# Authour : Rudra & Abhishek
# This code checks if a number is prime or not and calculate the factorial of the number
def fact(n):
    res=1
    for i in range(1,n+1):
        result*=i
    return res

def prime_check(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True