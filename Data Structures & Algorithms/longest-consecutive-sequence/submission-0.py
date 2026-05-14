class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsh = set(nums)

        longest = 0

        for num in numsh:
            if num-1 not in numsh:
                seq = [num]
                is_seq = True
                head = num+1
                while head in numsh:
                    seq.append(head)
                    head += 1
                longest = max(longest, len(seq))
        return longest