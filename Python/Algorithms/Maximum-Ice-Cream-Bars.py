class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if coins>=sum(costs):
            return len(costs)
        c = 0
        for i in sorted(costs):
            if i <= coins:
                c += 1
                coins -= i
            else:
                break
        return c
            
