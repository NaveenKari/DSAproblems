class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # My approach using dictionaries
        elements = set(nums)
        res = {}
        final = []
        for i in elements:
            res[i] = nums.count(i)
        # print(res)
        res1 = sorted(res.items(), key=lambda x: x[1])
        # print(res1)
        c=0
        for i in range(1,k+1):
            if c<k:
                final.append(res1[-i][0])
                c+=1
            else:
                break
        return final
    

# Optimised approach using Bucket sort 

        elements = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            elements[n] = 1+ elements.get(n,0)
        print(elements)
        for c,n in elements.items():
            freq[n].append(c)
        print(freq)
        res = []
        for i in range(len(nums),0,-1):
            if freq[i]:
                for j in freq[i]:
                    res.append(j)
            if len(res) == k:
                return res
          


                




        