import time
def computeLPSArray(pat, M, lps):
    len = 0
    lps[0] = 0
    i = 1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1

def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0]*M
    j = 0
    computeLPSArray(pat, M, lps)
    i = 0
    res = []
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            res.append(i-j)
            j = lps[j-1]
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return res

txt = input("Enter the text: ")
pat = input("Enter the pattern to be matched: ")
start_time = time.perf_counter()
result = KMPSearch(pat, txt)
end_time = time.perf_counter()
if not result:
    result = []
print("Match found at index: ", result)
print("Time taken: {:.6f} seconds".format(end_time - start_time))
