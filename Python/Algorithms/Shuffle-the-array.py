class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        t = []
        for i in range(n):
            t.append(nums[:n][i])
            t.append(nums[n:][i])
        return t
