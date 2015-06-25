class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):

        def product(list1, list2):
            result = []
            for item1 in list1:
                for item2 in list2:
                    result.append(item1 + item2)
            return result

        mapping = {'2': ['a', 'b', 'c'],
                   '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']}

        digit_list = []
        i = 0
        while i < len(digits):
            digit_list.append(digits[i])
            i = i + 1

        letter_list = []
        for digit in digit_list:
            letter_list.append(mapping[digit])

        if len(letter_list) == 0:
            result = [""]
        else:
            result = reduce(product, letter_list)
        return result