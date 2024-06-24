# Program to to determine all palindromic primes between two integers
# Ntobeko Mhlongo
# 26-04-2024
import sys
sys.setrecursionlimit (30000)
import math

def is_prime(n, divisor=2):
    """Checking if a number is prime number."""
    if n <= 1: # If the number is less ot equal to 1, it is not a prime number 
        return False
    if n == 2: # 2 is a prime number
        return True
    if divisor > math.isqrt(n): # If the divisor is greater than the square root of the number, it is a prime number
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor + 1) # Checking for the next divisor recursively

def is_palindrome(s):
    """Checking if a string is a palindrome."""
    if len(s) == 0 or len(s) == 1: # If the string is empty or has a single digit, it is a palindrome 
        return True
    if s[0] != s[-1]: # If the first character is not the same as the last character, the string is not a palindrome
        return False
    return is_palindrome(s[1:-1]) # Recursively checking if the middle part of the string is a palindrone

def find_palindrome_primes(N, M):
    """Finding all palindromic primes between N and M."""
    if N > M:
        return
    if is_prime(N) and is_palindrome(str(N)): # If N is is a prime number and a palindrome, print N
        print(N)
    find_palindrome_primes(N + 1, M)# Recursively checking for the next number

def main():
    N = int(input("Enter the starting point N:\n"))
    M = int(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    find_palindrome_primes(N, M)

if __name__ == '__main__':
        main()