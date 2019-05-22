def median_of_medians(L):
    if len(L) < 10:
        L.sort()
        return L[int(len(L)/2)]
    S = []
    lIndex = 0
    while lIndex+5 < len(L)-1:
        S.append(L[lIndex:lIndex+5])
        lIndex += 5
    S.append(L[lIndex:])
    Meds = []
    for subList in S:
        #print(subList)
        Meds.append(median_of_medians(subList))
    L2 = median_of_medians(Meds)
    L1 = L3 = []
    for i in L:
        if i < L2:
            L1.append(i)
        if i > L2:
            L3.append(i)
    if len(L) < len(L1):
        return median_of_medians(L1)
    elif len(L) > len(L1) + 1:
        return median_of_medians(L3)
    else:
        return L2
