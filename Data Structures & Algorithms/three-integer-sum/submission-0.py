class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # could pick one and then iterate through with two pointers
        # so we get n * n
        goal = 0
        solutions = []
        for i in range(len(nums)):
            # Iterate through the remaining with two pointers, like normal 2sum
            current = nums[i]
            toFind = - current
            
            solvedIndexes = {}
            for j in range(len(nums)):
                if i != j:
                    # Normal 2sum from here
                    needed = toFind - nums[j]
                    if needed in solvedIndexes.keys():
                        newList = [nums[i], nums[j], nums[solvedIndexes[needed]]]
                        newList.sort()
                        solutions.append(tuple(newList))
                    else:
                        solvedIndexes[nums[j]] = j
        
        # Now just iterate through and find the unique triplets
        

        return list(set(solutions))


            