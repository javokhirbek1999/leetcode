from heapq import heappush, heapreplace

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        t = 0
        cs = []
        for curr_cost, curr_end in sorted(courses, key=lambda x: x[1]):
            cc = -curr_cost
            if t <= curr_end + cc:
                heappush(cs, cc)
                t += curr_cost
            elif cs and cs[0] < cc:
                t += curr_cost + heapreplace(cs, cc)
        return len(cs)
