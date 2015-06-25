class Solution:
    # @return an integer
    def reverse(self, x):

        if (x == 0):
            return 0
        elif (x < 0):
            flag = -1
        else:
            flag = 1
    x = abs(x)
    result = 0
    while (x >= 10):
        last_digit = x % 10
        result = (result + last_digit) * 10
        x = x / 10
    result = flag * (result + x)
    if (result > 2147483647) or (result < -2147483648):
        return 0
    else:
        return result
