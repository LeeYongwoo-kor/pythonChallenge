upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = upper.lower()


def solution(s, n):
    for idx, char in enumerate(s):
        if char in upper:
            tIdx = (upper.index(char) + n) % 26
            s = s[0:idx] + upper[tIdx] + s[idx + 1 :]
        elif char in lower:
            tIdx = (lower.index(char) + n) % 26
            s = s[0:idx] + lower[tIdx] + s[idx + 1 :]

    return s

print(solution("ABCDEFG", 5))
print(solution("VWXYZ", 5))
print(solution("abcde", 10))