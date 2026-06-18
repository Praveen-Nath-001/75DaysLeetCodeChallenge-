class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==-2147483648 and divisor==-1:
            return 2147483647
        c=0
        flag=0
        if(dividend<0 and divisor<0):
            flag=0
        elif(dividend<0 or divisor<0):
            flag=1
        dividend=abs(dividend)
        divisor=abs(divisor)
        while(dividend>=divisor):
            t_divisor=divisor
            multiple=1
            while dividend>=(t_divisor<<1):
                t_divisor<<=1
                multiple<<=1
            dividend=dividend-t_divisor
            c=c+multiple
        if (flag == 1):
            return (c*-1)
        else:
            return(c)
        
        