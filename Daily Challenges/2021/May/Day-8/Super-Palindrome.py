class Solution:
    # -----------------------------TLE---------------------------------------------------------------
    # Works: But throws TLE
    # def superpalindromesInRange(self, left: str, right: str) -> int:
    #     c = 0
    #     i = 1
    #     while True:
    #         t = i*i
    #         if int(left)<=t<=int(right) and str(i)==str(i)[::-1] and str(t)==str(t)[::-1]:
    #             c+=1
    #         i+=1
    #         if t>=int(right):
    #             break
    #     return c
    # -----------------------------------------------------------------------------------------------
    def superpalindromesInRange(self, L: str, R: str) -> int:

	    def gen_palindromes(low, high):
		    res = []

		    def helper(string):
			    nonlocal L, length
			    if len(string) == L:
				    if length & 1:
					    res.extend([''.join(string + [str(i)] + string[::-1]) for i in range(10)])
				    else:
					    res.append(''.join(string + string[::-1]))
				    return None

			    for i in range(10):
				    if not i and not string:
					    continue
				    else:
					    helper(string + [str(i)])

		    for length in range(low, high + 1):
			    L = length // 2
			    helper([])

		    return res


	    a, b = int(L), int(R)
	    low = int(math.log10(a**0.5))+1
	    high = int(math.log10(b**0.5))+1
	    palindromes = gen_palindromes(low, high)

	    res = 0
	    for p in palindromes:
		    p = int(p)**2
		    if a <= p <= b:
			    p = str(p)
			    if p == p[::-1]:
				    res += 1
	    return res
