class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        cbmax = Counter()
        for b in B:
            cbmax |= Counter(b)
        return [a for a in A if not cbmax - Counter(a)]
