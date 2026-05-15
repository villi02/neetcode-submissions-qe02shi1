class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Thinking, how can we decide where a sequence starts?

        # using hashsets and checking if num-1 exists in the set
        longest = 0
        numsh = set(nums)
        for num in numsh:
            seq = 0
            if num-1 not in numsh:
                head = num
                while head in numsh:
                    seq = head-num+1
                    longest = max(longest, seq)
                    head += 1
        return longest