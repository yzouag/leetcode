class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum
        
        # method 1: using hashset to detect loop
        # numbers = set()
        # while n != 1 and n not in numbers:
        #     numbers.add(n)
        #     n = get_next(n)
        # return n == 1

        # method 2: using Floyd's Cycle Finding Algorithm
        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1
        

if __name__ == "__main__":
    n = 19
    assert True == Solution().isHappy(n)
    
    n = 2
    assert False == Solution().isHappy(n)