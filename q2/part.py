def partition(pivot,l, low, high):
	i = low
	j = high
	while i <= j:
		while l[i][0] < pivot: i += 1
		while l[j][0] > pivot: j -= 1
		if i <= j:
			l[i], l[j] = l[j], l[i]
			i, j = i + 1, j - 1
	return i-1

def partition2(pivot,arr,low,high): 
	i = ( low-1 )         # index of smaller element 
	#pivot = arr[high]     # pivot 

	for j in range(low , high): 
		# If current element is smaller than or 
		# equal to pivot 
		if   arr[j][0] <= pivot: 
			# increment index of smaller element 
			i = i+1 
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return i 

def my_partition( pivot, a_b,_i, _j):
    i = _i
    j = _j
    while (i != j):
        if (a_b[i][0] == a_b[j][0] and i < j):
            i+=1
        while (a_b[i][0] > pivot and i < j):
            i+=1
        while (a_b[j][0] < pivot and i < j):
            if (j == 0):
                break
            j-=1
        if (a_b[i][0] < a_b[j][0] ):
            aux = a_b[j]
            a_b[j] = a_b[i]
            a_b[i] = aux
    return j

#a = [6,50,4,3,2,10]
#print(partition(3,a,0,len(a)-1))
#print(a)