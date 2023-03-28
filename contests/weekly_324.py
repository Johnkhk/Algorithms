# Q2 Prime factorization
# https://www.youtube.com/watch?v=XBnUWjo3TgM&ab_channel=MathwithMr.J
class Solution:
    def smallestValue(self, n: int) -> int:
        """
        idea: use prime factorzation, and sum the primes
        e.g 15
        15%2 - Failed
        15%3 - Sucess 3*5
            s+3 = 3
            15//3 = 5
            
        5%3 - failed
        5%4 - Failed
        5%5 - Sucess 
            s+5 = 8
            5//5 = 0
        5%6 - failed
        5%7 - failed
        5%8 - failed
        .
        .
        5%15 - failed
        return s = 8
        """
        def primes(n, s=0):
            for i in range(2,n+1):
                while n % i == 0:
                    s += i
                    n //= i
            return s
        prev = n
        cur = primes(n)
        while prev != cur:
            prev = cur
            cur = primes(cur)
        return cur
        
#         # while n != (n:=primes(n)): pass
#         while n!=primes(n):
#             n = primes(n)
#             print(n)
#             break
        
#         return n

# Q3 2508. Add Edges to Make Degrees of All Nodes Even