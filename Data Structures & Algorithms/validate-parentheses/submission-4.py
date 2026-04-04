class Solution:
    def isValid(self, s: str) -> bool:
        # I think we should make a dqueue, then simply pop
        ismorph = {}
        ismorph["("] = ")"
        ismorph["{"] = "}"
        ismorph["["] = "]"

        queue = deque()
        for char in s:
            if (char == "(") or (char == "[") or (char == "{"):
                queue.append(ismorph[char])
            else:
                if not queue:
                    return False
                comp_char = queue.pop()
                if char != comp_char:
                    return False
        
        return len(queue) == 0
