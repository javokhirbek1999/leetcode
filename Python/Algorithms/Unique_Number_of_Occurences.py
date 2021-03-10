class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        li = []
        l = set(arr)
        for i in l:
            li.append(arr.count(i))
        t = len(set(li))
        r = len(li)
        return t == r
            
