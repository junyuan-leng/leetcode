class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        # words_list = map(lambda word : word.strip(), s.strip().split())
        words_list = s.strip().split()
        return (' ').join(words_list[::-1])
