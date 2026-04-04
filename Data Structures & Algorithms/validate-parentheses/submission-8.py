class Solution:
    def isValid(self, s: str) -> bool:
        right = ["]", ")", "}"]
        left = ["[", "{", "("]

        match = {"[": "]", "{": "}", "(": ")"}

        left_stack = []
        for char in s:
            if char in right:
                if len(left_stack) == 0:
                    return False
                left_popped = left_stack.pop()
                if char != match[left_popped]:
                    return False
            else:
                left_stack.append(char)
        return len(left_stack) == 0