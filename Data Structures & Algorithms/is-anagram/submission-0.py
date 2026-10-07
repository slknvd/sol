class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s2 = sorted(list(s))
        t2 = sorted(list(t))
        if s2 == t2:
            return True
        else:
            return False

        