class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for i in numSet:
            if (i-1) not in numSet:
                length = 1
                while (i+length) in numSet:
                    length+=1
                res = max(res,length)
        return res
    


# To find start element we need to check previous element present in the set or not.