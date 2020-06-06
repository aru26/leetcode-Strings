class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = s.lower();
        s = re.sub('[^a-z0-9]','',s) # 正則表達式去除非字母和數字
        if s == s[::-1]: 
            return True;
        else:
            return False;
            
 
