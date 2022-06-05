class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source == destination:
            return True
        
        if not edges and source != destination:
            return False
        
        graph = {}
        
        for i,j in edges:
            if i not in graph:
                graph[i] = [j]
            else:
                graph[i].append(j)
                
            if j not in graph:
                graph[j] = [i]
            else:
                graph[j].append(i)
            
        stack = [source]
        visited = {}
        while stack:
            
            vertex = stack.pop()
            visited[vertex] = 1
            if vertex == destination:
                return True
            
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)
        
        
        return False
