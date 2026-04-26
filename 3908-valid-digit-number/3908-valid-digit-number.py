class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        new_str = str(n)
        new_x = str(x)
        if new_x in new_str and new_x != new_str[0]:
            return True 
        else:
            return False

        