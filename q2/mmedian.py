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



import sys, random


items_per_column = 15


def find_i_th_smallest( A, i ):
    t = len(A)
    if(t <= items_per_column):
        # if A is a small list with less than items_per_column items, then:
        #     1. do sort on A
        #     2. return the i-th smallest item of A
        #
        return sorted(A)[i]
    else:
        # 1. partition A into columns of items_per_column items each. items_per_column is odd, say 15.
        # 2. find the median of every column
        # 3. put all medians in a new list, say, B
        #
        B = [ find_i_th_smallest(k, (len(k) - 1)/2) for k in [A[j:(j + items_per_column)] for j in range(0,len(A),items_per_column)]]

        # 4. find M, the median of B
        #
        M = find_i_th_smallest(B, (len(B) - 1)/2)

        # 5. split A into 3 parts by M, { < M }, { == M }, and { > M }
        # 6. find which above set has A's i-th smallest, recursively.
        #
        P1 = [ j for j in A if j < M ]
        if(i < len(P1)):
            return find_i_th_smallest( P1, i)
        P3 = [ j for j in A if j > M ]
        L3 = len(P3)
        if(i < (t - L3)):
            return M
        return find_i_th_smallest( P3, i - (t - L3))
