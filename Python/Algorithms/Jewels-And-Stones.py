class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = 0
        l = list(stones)
        for i in range(len(jewels)):
            c+= l.count(jewels[i])
        return c
