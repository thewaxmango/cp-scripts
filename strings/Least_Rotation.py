# FROM PYRIVAL

# returns starting index of lexicographically smallest rotation of a string
def Least_Rotation(s: str) -> int:
    a, n = 0, len(s)
    s = s * 2

    b = 1
    while b < n:
        for i in range(b - a):
            if s[a + i] > s[b + i]:
                a = b
                b += 1
                break
            if s[a + i] < s[b + i]:
                b += i + 1
                break
        else:
            b += b - a
    return a

print(Least_Rotation("baquana"))