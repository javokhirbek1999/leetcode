class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        graph = {}
        
        for i, j in edges:
            
            if i not in graph:
                graph[i] = [j]
            else:
                graph[i].append(j)
            
            if j not in graph:
                graph[j] = [i]
            else:
                graph[j].append(i)
        
        
        print(graph)
        for i in graph.keys():
            if len(graph.keys())-1 == len(graph[i]):
                return i
