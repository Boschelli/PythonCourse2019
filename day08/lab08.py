## Exercise 1
## Write a function using recursion to calculate the greatest common divisor of two numbers

## Helpful link:
## https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
def gcd(x, y):
    if x==0:
        return y
    if y==0:
        return x
    return gcd(y,x%y)
gcd(108,96)



result=[1,3,5]
0 not in [25%i for i in result[1:]]
print(result)
## Problem 2
## Write a function using recursion that returns prime numbers less than 121

import time

def find_primes(me = 121, primes = []):
    if me==2:
        primes.append(2)
        return primes
    if me%2==0:
        find_primes(me-1,primes)
        return primes
    find_primes(me-1,primes)
    if 0 not in [me%i for i in primes[2:]]:
        primes.append(me)
    return primes


start = time.time()
find_primes(2000,[])
end = time.time()
print(end - start)




## Problem 3
## Write a function that gives a solution to Tower of Hanoi game
## https://www.mathsisfun.com/games/towerofhanoi.html




def move_rings(n,current,destination,open):
