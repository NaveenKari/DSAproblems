class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            check = target - nums[i]
            temp = nums[i+1:]
            # print(temp)
            # print(check)
            if check in temp:
                res.append(i)
                x = temp.index(check)
                res.append(x+(i+1))
                break
        return res