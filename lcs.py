def lcs(X, Y):
    m = len(X)
    n = len(Y)
    # An (m+1) times (n+1) matrix
    C = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
    return C


def back_track(C, X, Y, i, j):
    if i == 0 or j == 0:
        return ""
    elif X[i-1] == Y[j-1]:
        return back_track(C, X, Y, i-1, j-1) + X[i-1]
    else:
        if C[i][j-1] > C[i-1][j]:
            return back_track(C, X, Y, i, j-1)
        else:
            return back_track(C, X, Y, i-1, j)


X = "AATCC"
Y = "ACACG"
m = len(X)
n = len(Y)
C = lcs(X, Y)

for c in C:
    print c
print "One LCS:", back_track(C, X, Y, m, n)