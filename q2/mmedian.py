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

def mm(A, i):
    i = int(i)
    #divide A into sublists of len 5
    sublists = [A[j:j+5] for j in range(0, len(A), 5)]
    medians = [sorted(sublist)[int(len(sublist)/2)] for sublist in sublists]
    if len(medians) <= 5:
        print(int(len(medians)/2))
        pivot = sorted(medians)[int(len(medians)/2)]
    else:
        #the pivot is the median of the medians
        pivot = mm(medians, int(len(medians)/2))

    #partitioning step
    low = [j for j in A if j < pivot]
    high = [j for j in A if j > pivot]

    k = len(low)
    if i < k:
        return mm(low,i)
    elif i > k:
        return mm(high,i-k-1)
    else: #pivot = k
        return pivot

import sys, random


items_per_column = 15


def find_i_th_smallest( A, i ):
    t = len(A)
    i = int(i)
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



def select(A, i):
    i = int(i)
    if len(A) <= 5:
        try:
            return sorted(A)[i]
        except IndexError:
            print(A)
            print(i)
            return A[i-1]
            a = 2/0
    chunks = [A[i : i + 5] for i in range(0, len(A), 5)]
    medians = [select(chunk, len(chunk) // 2) for chunk in chunks]
    medianOfMedians = select(medians, len(medians) // 2)
    lowerPartition, upperPartition = (
        [a for a in A if a < medianOfMedians],
        [a for a in A if a > medianOfMedians],
    )
    if i == len(lowerPartition):
        return medianOfMedians
    elif i > len(lowerPartition):
        return select(upperPartition, i - len(lowerPartition) - 1)
    else:
        return select(lowerPartition, i)

def mediana_das_medianas(A):

    #divide A into sublists of len 5
    sublists = [sorted(A[j:j+5]) for j in range(0, len(A), 5)]
    medians = [sublist[len(sublist)//2] for sublist in sublists]

    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians)//2]
    else:
        #the pivot is the median of the medians
        #pivot = median_of_medians(medians, len(medians)//2)
        pivot = mediana_das_medianas(medians)

    return pivot


"""
def mediana_das_medianas(vet):

    aux =[]
    unsigned int k, i

    for k in range(0,len(vet),5):
        if ((k+4) < len(vet))
            my_insert_sort(vet,k,k+4)
        else:
            my_insert_sort(vet,k,len(vet)-1)
    
    if (len(vet) >= 5)
        aux.resize(k/5)
    else:
        k = len(vet)/2
        return vet[k]

    k = 0
    
    for i in range(2,len(vet),5):
        if (k == aux.size())
            aux.resize(k+1)
        aux[k++] = vet[i]
    return mediana_das_medianas(aux)
"""