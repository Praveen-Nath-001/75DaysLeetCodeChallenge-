class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        number_str = str(n)
        digit_x = str(x)
        if digit_x in number_str and digit_x != number_str[0]:
            return True 
        else:
            return False

        