# From YOSUPO LIBRARY CHECKER
# Finds the length of the longest palindrome about and between each character

def Manacher(s: str):
	S = s.replace('', '#')
	return Manacher_Odd(S)

def Manacher_Odd(s: str):
    n = len(s)
    p = [1 for _ in range(n)]
    c = 0
    for i in range(1, n):
        if i < c + p[c]:
            p[i] = min(p[c - (i - c)], c + p[c] - i)
        while i - p[i] >= 0 and i + p[i] < n and s[i - p[i]] == s[i + p[i]]:
            p[i] += 1
        if i + p[i] > c + p[c]:
            c = i
    return [(2 * p[i] - 1) // 2 for i in range(1, n - 1)]

if __name__ == "__main__":
	print(Manacher("Mississippi"))