import time

def BoyerMoore(txt, pat):
    m = len(pat)
    n = len(txt)
    res = []
    # create the bad character heuristic lookup table
    badChar = [-1]*256
    for i in range(m):
        badChar[ord(pat[i])] = i
    # s is the shift of the pattern with respect to text
    s = 0
    start_time = time.perf_counter()
    while s <= n-m:
        j = m-1
        while j>=0 and pat[j] == txt[s+j]:
            j -= 1
        if j<0:
            res.append(s)
            s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)
        else:
            s += max(1, j-badChar[ord(txt[s+j])])
    end_time = time.perf_counter()
    if res:
        print("Match found at index: ", res)
        print("Time taken: {:.6f} seconds".format(end_time - start_time))
    else:
        print("No match found")
        print("Time taken: {:.6f} seconds".format(end_time - start_time))

txt = input("Enter the text: ")
pat = input("Enter the pattern to be matched: ")
BoyerMoore(txt, pat)
