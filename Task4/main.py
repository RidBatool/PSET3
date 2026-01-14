def find_anagrams(s, p):
    result = []
    n, m = len(s), len(p)

    if n < m:
        return []

    count_p = [0] * 26
    for ch in p:
        count_p[ord(ch) - ord('a')] += 1

    window = [0] * 26
    for ch in s[:m]:
        window[ord(ch) - ord('a')] += 1

    if window == count_p:
        result.append(0)

    for i in range(m, n):
        window[ord(s[i - m]) - ord('a')] -= 1
        window[ord(s[i]) - ord('a')] += 1

        if window == count_p:
            result.append(i - m + 1)

    return result


s = "cbaebabacd"
p = "abc"
print(find_anagrams(s, p))
