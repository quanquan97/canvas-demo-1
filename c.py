class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x >= 0 or x < 10:
            return True
        if x >= 10 or x < 100:
            str_x = str(x)
            if str_x[1] == str_x[2]:
                return True
            else:
                return False
        if x >= 100:
            if str_x[::-1] == str_x:
                return True
            else:
                return False
