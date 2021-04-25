class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        dicSet = defaultdict(set)
        for i,j in connections:
            dicSet[i].add(j)
            dicSet[j].add(i)
        down = {}
        res = []
        def visited(node,from_node = None):
            if node in down: 
                return down[node]
            cur_ind = down[node] = len(down)
            for near in dicSet[node]:
                if near == from_node:
                    continue
                down[node] = min(down[node],visited(near,node))
            if cur_ind == down[node] and from_node is not None:
                res.append([from_node,node])  
            return down[node]
        visited(0)
        return res
