# pi[i] = max(k for k in range(i) if S[0:k-1] = S[i-(k-1):i])
# Length of longest nontrivial substring that is prefix of S and suffix of S[:i]

def KMP(s: str) -> list[int]:
	n = len(s)
	pi_s = [0] * n
	j = 0
	for i in range(1, n):
		while j > 0 and s[j] != s[i]:
			j = pi_s[j - 1]
		if s[i] == s[j]:
			j += 1
		pi_s[i] = j
	return pi_s

if __name__ == "__main__":
    print(KMP("abcabcd"))