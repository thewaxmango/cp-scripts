# From YOSUPO LIBRARY CHECKER

# z[i] = max(k for k in range(len(S)-i) if S[0:k-1] = S[len(S)-k:])
# Length of longest nontrivial substring that is prefix of S and suffix of S[i:]

def Z(s: str) -> list[int]:
	N = len(s)
	z = [0]*N
	z[0] = N
	l, r = 0, 0
	for i in range(1, N):
		z[i] = max(0, min(r - i, z[i - l]))
		while i + z[i] < N and s[z[i]] == s[i + z[i]]:
			z[i] += 1
		if i + z[i] > r:
			l, r = i, i + z[i]
	return z

if __name__ == "__main__":
    print(Z("abcbcba"))