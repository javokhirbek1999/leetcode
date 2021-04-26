class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        max_heap = []
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1]
            if diff <= 0:
                continue
            else:
                heappush(max_heap, -diff)
                
                while bricks < diff:
                    if ladders <= 0 or len(max_heap) <= 0:
                        return i - 1
                    bricks += -1 * heappop(max_heap)
                    ladders -= 1
                
                bricks -= diff
        
        return len(heights) - 1
