class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Going to use isInstance(x, int)
        # Why cant we just iterate through and just if there is a non int, then simply operate on the two previous elements. Remember to then add the result to the stack

        if len(tokens) < 3:
            return int(tokens[0])

        stack = []
        for val in tokens:
            if val in ["+", "*", "-", "/"]:
                val1 = stack.pop()
                val2 = stack.pop()
                print(f"Operating: {val2} {val} {val1}")
                newVal = self.operate(val2, val1, val)
                stack.append(newVal)
            else:
                stack.append(int(val))
        print(f"stack at the end: {stack}")
        return stack[-1]

    def operate(self, x, y, op):
        if op == "+":
            return x+y
        elif op == "-":
            return x-y
        elif op == "*":
            return x*y
        elif op == "/":
            return int(x/y)
                