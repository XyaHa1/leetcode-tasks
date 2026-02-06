def cache(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        cache[args] = func(*args)
        return cache[args]
    return wrapper


class Solution:
    @cache
    def square(self, n: int) -> int:
        return n ** 2

    def sumOfSquares(self, n: int) -> int:
        squares = 0
        while n != 0:
            squares = squares + self.square(n % 10)
            n //=10
        return squares

    def isHappy(self, n: int) -> bool:
        cache = set()
        num = n
        while num != 1:
            num = self.sumOfSquares(num)
            if num in cache:
                return False
            cache.add(num)
        return True
    

if __name__ == '__main__':
    print(Solution().isHappy(19))