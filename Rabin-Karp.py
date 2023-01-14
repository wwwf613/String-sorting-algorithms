import time

def RabinKarpSearch(pat, txt, d, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0    # hash value for pattern
    t = 0    # hash value for txt
    h = 1
    result = []

    # The value of h would be "pow(d, M-1)%q"
    for i in range(M-1):
        h = (h*d)%q

    # Calculate the hash value of pattern and first window of text
    for i in range(M):
        p = (d*p + ord(pat[i]))%q
        t = (d*t + ord(txt[i]))%q

    # Slide the pattern over text one by one
    for i in range(N-M+1):
        # Check the hash values of current window of text and pattern
        # If the hash values match then only check for characters on by one
        if p==t:
            # Check for characters one by one
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
            j+=1
            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j==M:
                result.append(i)
        # Calculate hash value for next window of text: Remove leading digit, add trailing digit
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i + M]))%q
            if t < 0:
                t = t+q
    if result:
        return result
    else:
        return "No match found"

txt = input("Enter the text: ")
pat = input("Enter the pattern to be matched: ")
start_time = time.perf_counter()
result = RabinKarpSearch(pat, txt, d=256, q=101)
end_time = time.perf_counter()

if result != "No match found":
    print("Match found at index: ", result)
    print("Time taken: {:.6f} seconds".format(end_time - start_time))
else:
    print(result)
    print("Time taken: {:.6f} seconds".format(end_time - start_time))

