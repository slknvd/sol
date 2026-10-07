import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = "".join(ch.lower() for ch in s if ch.isalnum())
        left = 0
        right = len(s2) - 1
        while left <= right:
            if s2[left] != s2[right]:
                return False
            else:
                left += 1
                right -= 1
        return True