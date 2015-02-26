class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A is None or len(A) == 0:
            return 0
        elif len(A) == 1:
            return 1
        else:
            length = len(A)
            for i in range(len(A)-1):
                if A[i] == A[i+1]:
                    length = length - 1
            return length