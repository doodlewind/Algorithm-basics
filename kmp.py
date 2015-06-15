def build_prefix(pattern):
    prefix = [0 for i in range(len(pattern))]
    k = 0
    for q in range(1, len(pattern)):
        while k > 0 and pattern[k] != pattern[q]:
            k = prefix[k]
        if pattern[k] == pattern[q]:
            k += 1
        prefix[q] = k
    return prefix

def kmp(pattern, text, prefix):
    q = 0
    for i in range(0, len(text)):
        while q > 0 and pattern[q] != text[i]:
            q = prefix[max(q-1, 0)]
        if pattern[q] == text[i]:
            q += 1
        if q == len(pattern):
            print "match at text[%d]" % (i - len(pattern) + 1)
            q = prefix[max(q-1, 0)]


p = "abcdabd"
t = "abcdabxabcdabcdabde"
pre = build_prefix(p)
kmp(p, t, pre)
