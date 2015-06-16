def build_prefix(pattern):
    prefix, k = [0], 0
    for q in range(1, len(pattern)):
        while k > 0 and pattern[k] != pattern[q]:
            k = prefix[k]
        if pattern[k] == pattern[q]:
            k += 1
        prefix.append(k)
    return prefix

def kmp(pattern, text, prefix):
    q = 0
    for i in range(0, len(text)):
        while pattern[q] != text[i] and q > 0:
            q = prefix[q-1]
        if pattern[q] == text[i]:
            q += 1
        if q == len(pattern):
            print "match at text[%d]" % (i - len(pattern) + 1)
            q = prefix[q-1]


p = "abcdabd"
t = "abcdabxabcdabcdabde"
pre = build_prefix(p)
kmp(p, t, pre)
