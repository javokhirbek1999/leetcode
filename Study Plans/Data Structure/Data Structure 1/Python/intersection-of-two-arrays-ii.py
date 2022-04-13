class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = {}
        n2 = {}
        
        for i in nums1:
            if i not in n1:
                n1[i] = 1
            else:
                n1[i]+=1
        
        for i in nums2:
            if i not in n2:
                n2[i] = 1
            else:
                n2[i]+= 1
        
        res = []
        
        for i in n1.keys():
            if i in n2:
                res.extend([i]*min(n1[i], n2[i]))

        return res
