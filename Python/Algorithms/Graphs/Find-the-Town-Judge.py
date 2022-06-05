class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if not trust and n == 1:
            return 1
        
        if not trust and n > 1:
            return -1
        
        graph = {}
        
        for i,j in trust:
            
            if i not in graph:
                graph[i] = [j]
            else:
                graph[i].append(j)
        
        # Find the major
        major = 0
        for i in range(1, n+1):
            if i not in graph:
                major = i
        
        # Make sure that everybody trusts him -> confirming if he is a real major
        for i in graph.values():
            if major not in i:
                return -1
        return major
