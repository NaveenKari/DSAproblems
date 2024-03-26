class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            lt=set(s)
            for i in lt:
                if s.count(i) == t.count(i):
                    continue
                else :
                    return False
            return True
        else:
            return False
            