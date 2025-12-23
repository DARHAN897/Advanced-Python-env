S1 = input()
S2 = input()

if len(S1) != len(S2):
    print("NO")
else:
    counts1 = {}
    counts2 = {}
    
    for ch in S1:
        if ch in counts1:
            counts1[ch] += 1
        else:
            counts1[ch] = 1
            
    for ch in S2:
        if ch in counts2:
            counts2[ch] += 1
        else:
            counts2[ch] = 1
    
    if counts1 == counts2:
        print("YES")
    else:
        print("NO")