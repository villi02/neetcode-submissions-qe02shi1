class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Want to have one pointer at each end of the word, and then iterate through, skipping any space
        back, front = 0, len(s) - 1

        while front > back:
            while front > back and not (ord("A") <= ord(s[back]) <= ord("Z") or ord("a") <= ord(s[back]) <= ord("z") or ord("0") <= ord(s[back]) <= ord("9")):
                back += 1
            while front > back and not (ord("A") <= ord(s[front]) <= ord("Z") or ord("a") <= ord(s[front]) <= ord("z") or ord("0") <= ord(s[front]) <= ord("9")):
                front -= 1
            if s[front].lower() != s[back].lower():
                return False
            back += 1
            front -= 1
        return True
        