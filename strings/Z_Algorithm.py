# Translated from USACO GUIDE

# z[i] = max(k for k in range(len(S)-i) if S[0:k-1] = S[len(S)-k:])
# Length of longest nontrivial substring that is prefix of S and suffix of S[i:]

def Z(s: str) -> list[int]:
	n = len(s)
	z_s = [0] * n
	z_s[0] = n
	l, r = 0, 0
	for i in range(1, n):
		z_s[i] = max(0, min(z_s[i - l], r - i + 1))
		while i + z_s[i] < n and s[z_s[i]] == s[z_s[i] + i]:
			l = i
			r = i + z_s[i]
			z_s[i] += 1
	return z_s

if __name__ == "__main__":
    print(Z("aabxaayaab"))