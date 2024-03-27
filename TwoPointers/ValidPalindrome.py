class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==1 or s == ' ':
            return True
        else:
            t=''
            for i in s:
                i=i.lower()
                if i.isalnum():
                    t+=i
            left = 0
            right = len(t)-1
            while left < right:
                if t[left] == t[right]:
                    left +=1
                    right-=1
                    continue
                else:
                    return False
            return True
                    
