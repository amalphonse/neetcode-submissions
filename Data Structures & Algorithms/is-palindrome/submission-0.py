class Solution:
    def isPalindrome(self, s: str) -> bool:
        text=''.join(filter(str.isalnum,s.lower()))
        rev_text=text[::-1]
        return text==rev_text