class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for d in s: 
            if d.isalnum():
                newStr += d.lower()
        return newStr == newStr[::-1]