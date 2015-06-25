class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                op2 = stack.pop()
                op1 = stack.pop()
                if token == '+':
                    res = int(float(op1) + float(op2))
                elif token == '-':
                    res = int(float(op1) - float(op2))
                elif token == '*':
                    res = int(float(op1) * float(op2))
                elif token == '/':
                    res = int(float(op1) / float(op2))
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[0]