class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        vals = []
        operations = ["+", "*", "/", "-"]

        for i, char in enumerate(tokens):
            if char in operations:
               first_operand = vals.pop()
               second_operand = vals.pop()
               new_operand = self.operate(second_operand, first_operand, char)
               vals.append(int(new_operand))
            else:
                vals.append(int(char))
        return vals[-1]
    
    def operate(self, current_sum, new_factor, char):
        if char == "+":
            current_sum += new_factor
        elif char == "*":
            current_sum *= new_factor
        elif char == "/":
            current_sum /= new_factor
        elif char == "-":
            current_sum -= new_factor
        return current_sum