class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=nums.count(0)
        if a==1:
            r=[0]*len(nums)
            pos=0
            m=1
            for i in nums:
                if i!=0:
                    m*=i
            #print(m)
            pos=nums.index(0)
            #print(pos)
            r[pos]=m
            return r
        elif a>1:
            r=[0]*len(nums)
            return r
        
        else:
            m=1
            r=[]
            for i in nums:
                m*=i
            for i in nums:
                a=m//i
                r.append(a)
            return r
