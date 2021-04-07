class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a,b = s[:len(s)//2],s[len(s)//2:]
        ac,bc = 0,0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        for i in a:
            if i in vowels:
                ac+=1

        for i in b:
            if i in vowels:
                bc+=1
                
        return ac==bc  
