class Solution:
# @return a boolean
    def isPalindrome(self, x):
        if (x < 0):
            return False
        origin = x
        result = 0
        while (x != 0):
            result = result * 10 + x % 10
            x = x / 10
        return origin == result
