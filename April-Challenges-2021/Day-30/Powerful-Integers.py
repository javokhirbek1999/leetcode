class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        p = []
        for i in range(20):
            for j in range(20):
                t = x**i+y**j
                if t <= bound and t not in p:
                    p.append(t)
        return sorted(p)
