class Solution:
    def isPalindrome(self, s: str) -> bool:
        # basically use two pointers, one from the left and one from the right and if they dont match, or go past each other, then return False, else True
        left = 0
        right = len(s) - 1

        while left < right:
            while right > left and not (ord("A") <= ord(s[left]) <= ord("Z") or ord("a") <= ord(s[left]) <= ord("z") or ord("0") <= ord(s[left]) <= ord("9")):
                left += 1
            while right > left and not (ord("A") <= ord(s[right]) <= ord("Z") or ord("a") <= ord(s[right]) <= ord("z") or ord("0") <= ord(s[right]) <= ord("9")) and right > 0:
                right -= 1
        
            
            if s[left].lower() != s[right].lower():
                print(f"{s[left]} is not {s[right]}")
                return False
            print(f"{s[left]} is the same as {s[right]}")
            left += 1
            right -= 1
        return True