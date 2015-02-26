class Solution:
    # @return an integer
    def atoi(self, str):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        flags = ['+', '-']
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        s = str.strip()
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            if s in digits:
                return int(s)
            else:
                return 0
        else:
            if s[0] not in flags and s[0] not in digits:
                return 0
            elif s[0] == '+':
                flag = 1
                s = s[1:]
            elif s[0] == '-':
                flag = -1
                s = s[1:]
            else:
                flag = 1
            temp = 0
            for digit in s:
                if digit in digits:
                    temp = temp * 10 + int(digit)
                else:
                    break
            result = temp * flag
            if result > INT_MAX:
                return INT_MAX
            elif result < INT_MIN:
                return INT_MIN
            else:
                return result
