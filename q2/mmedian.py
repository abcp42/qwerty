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


items_per_column = 5


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
def nlogn_median(l):
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[int(len(l) / 2)]
    else:
        return 0.5 * (l[int(len(l) / 2) - 1] + l[int(len(l) / 2)])

import random
def quickselect_median(l, pivot_fn=random.choice):
    if len(l) % 2 == 1:
        return quickselect(l, len(l) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect(l, len(l) / 2 - 1, pivot_fn) +
                      quickselect(l, len(l) / 2, pivot_fn))


def quickselect(l, k, pivot_fn=random.choice):
    """
    Select the kth element in l (0 based)
    :param l: List of numerics
    :param k: Index
    :param pivot_fn: Function to choose a pivot, defaults to random.choice
    :return: The kth element of l
    """
    if len(l) == 1:
        #assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # We got lucky and guessed the median
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


def pick_pivot(l):
    """
    Pick a good pivot within l, a list of numbers
    This algorithm runs in O(n) time.
    """
    assert len(l) > 0

    # If there are < 5 items, just return the median
    if len(l) < 5:
        # In this case, we fall back on the first median function we wrote.
        # Since we only run this on a list of 5 or fewer items, it doesn't
        # depend on the length of the input and can be considered constant
        # time.
        return nlogn_median(l)

    # First, we'll split `l` into groups of 5 items. O(n)
    chunks = chunked(l, 5)

    # For simplicity, we can drop any chunks that aren't full. O(n)
    #full_chunks = [chunk for chunk in chunks if len(chunk) == 5]
    full_chunks = chunks

    # Next, we sort each chunk. Each group is a fixed length, so each sort
    # takes constant time. Since we have n/5 chunks, this operation
    # is also O(n)
    sorted_groups = [sorted(chunk) for chunk in full_chunks]

    # The median of each chunk is at index 2
    medians = [chunk[int(len(chunk)/2)] for chunk in sorted_groups]

    # It's a bit circular, but I'm about to prove that finding
    # the median of a list can be done in provably O(n).
    # Finding the median of a list of length n/5 is a subproblem of size n/5
    # and this recursive call will be accounted for in our analysis.
    # We pass pick_pivot, our current function, as the pivot builder to
    # quickselect. O(n)
    median_of_medians = quickselect_median(medians, pick_pivot)
    return median_of_medians

def chunked(l, chunk_size):
    """Split list `l` it to chunks of `chunk_size` elements."""
    return [l[i:i + chunk_size] for i in range(0, len(l), chunk_size)]

import time
import numpy as np

l = []
for i in range(100):
    l.append(random.random())
#l = [6,5,4,3,2,1]
start_time = time.time()
a =quickselect(l,len(l)/2)
print("--- %s seconds ---" % (time.time() - start_time))

print(a)
start_time = time.time()
a = pick_pivot(l)
print("--- %s seconds ---" % (time.time() - start_time))

print(a)
start_time = time.time()
print(find_i_th_smallest(l,len(l)/2))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(np.partition(l, int(len(l)/2))[int(len(l)/2)] )
print("--- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
print(nlogn_median(l))
print("--- %s seconds ---" % (time.time() - start_time))
