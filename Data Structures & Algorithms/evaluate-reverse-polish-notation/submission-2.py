class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        # prev_val = tokens[0]
        # curr_val = tokens[1]
        # result = 0
        stack = []
        for tk in tokens:
            if tk in '+-*/':
                b = stack.pop()
                a = stack.pop()

                if tk == '+':
                    stack.append(a + b)
                elif tk == '-':
                    stack.append(a - b)
                elif tk == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))

            else:
                stack.append(int(tk))
        return stack[0]
