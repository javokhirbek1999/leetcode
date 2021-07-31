class Solution:
    def reverse(self, x: int) -> int:
        temp = ''
        if x<0:
            x = x//-1
            temp+='-'
            temp+="".join(list(str(x))[::-1])
        else:
            temp+="".join(list(str(x))[::-1])
        temp = int(temp)
        mn,mx = pow(2,31)//-1,pow(2,31)-1
        if mn <= temp <=mx:
            return temp
        return 0
        
