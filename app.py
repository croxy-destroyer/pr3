# Project : Prime-check + Factorial
# Authour : Abhishek
# This code checks if a number is prime or not and calculate the factorial of the number
def prime_check(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True