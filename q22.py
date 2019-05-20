import CPUtimer

class AB():
	def __init__(self):
		self.ab_razao = []
		self.ab_ind = []

	def put(self,razao,ind):
		self.ab_razao.append(razao)
		self.ab_ind.append(ind) 
	
	def get_razao(self,ind):
		return ab_razao[ind]



def gera_ab(A,B):
	if(len(A)!=len(B)):
		raise Exception('A and B have different lenghts')
	r = A[0]/B[0]
	#vec = AB() 
	vec = []
	for i in range(len(A)):
		#vec.put(A[i]/B[i],i)
		vec.append((A[i]/B[i],i))
	return vec

def update(A,B,S):
	ao = A[0]
	bo = B[0]
	for i in range(len(S)):
		if(S[i]==1):
			ao+=A[i]
			bo+=B[i]
	return ao/bo

def alg1(A,B):
	ab = gera_ab(A,B)
	razao1 = ab[0][0]#na pos 0, pegue o indice 0 da tuple, que é a razão 
	R_star = razao1 # variavel para encontra R*
	#lista de indice com N elementos
	S_star = [] # S*
	S = []
	x = []
	for i in range(1,len(A)+1):
		S.insert(i,0)

	cond = True
	while(1):#enquanto todos os elementos não tiverem sido averiguados. O(n)
		cond = True #Enquanto houver alguem em S que satisfaz as 2 condicoes, o alg continua rodando
		print('S:',S)
		print('R_star:',R_star)
		for i in range(len(S)): #pior caso O(n)
			print('ab[i][0]:',ab[i][0])
			if S[i] == 0  and ab[i][0] > R_star: # O(1)
				S[i] = 1
				cond = False
				break
			elif S[i] == 1  and ab[i][0] < R_star: #nao satisfaz o lema
				S[i] = 0
				cond = False
				break
		if(cond):
			break
		R_star = update(A,B,S)

	#Ao fim do algoritmo, somente os valores otimos devem ficar em S, sendo assim o S*
	print('S_star: ',S)
	print('R_star: ',R_star)



def algoritmo1(A,B):
	ab = gera_ab(A,B)
	razao1 = ab[0][0]#na pos 0, pegue o indice 0 da tuple, que é a razão 
	R_star = razao1 # variavel para encontra R*
	#lista de indice com N elementos
	ind_list = [i for i in range(len(A))]#lista de indices: Desse modo, sempre sabemos onde esta cada elemento
	S_star = [] # S*
	while(len(ind_list)!=0):#enquanto todos os elementos não tiverem sido averiguados. O(n)
		k = ind_list[0] #pega o primeiro elemento
		ind_list=ind_list[1:] #retira da lista esse primeiro elemento

		if(ab[k][0] > R_star): # se a razao do par iterado atualmente for maior que o R* atual
			S_star.append(k)
			sum_a = A[0]
			sum_b = B[0]
			for s in S_star:#some todos no subconjunto otimo. O(n^2)
				sum_a += A[s]
				sum_b += B[s]
			Rs = sum_a/sum_b#calcule a razao das somas(equacao Rs)
			if (R_star < Rs): # Se a razao otima R* for menor que a razao atual R(S)
				R_star = Rs;
				while (len(S_star)>0): #Retira todos que estavam no subconjunto otimo S* e coloque na lista. O(n^2)
					s = S_star.pop()#pega o ultimo elemento
					ind_list.append(s)
					#S_star = S_star[:-1] #retira o ultimo elemento
	print('S_star: ',S_star)
	print('ind_list: ',ind_list)

#Gera as razões entre A e B. Sorteia essas razões em nlogn(Merge por ex.). Pegue a razao
#de Ao e Bo e vai iterando enquanto soma as razoes dos demais índices. Pelo lema, 
#somente se um par at/bt > R* ele pode ser adicionado ao conjunto ótimo S*
def algoritmo2(A,B):
	ab = gera_ab(A,B)

	ab = sorted(ab, key=lambda tup: tup[0]) #sorteia pela razao, nlogn
	sum_a = A[0]
	sum_b = B[0]
	i = 1;
	while(i < len(ab)):#percorra todos elementos

		k = ab[i][1];

		rs = (sum_a+A[k])/(sum_b+B[k])
		if (ab[i][0] > rs): # se a razao do elemento for maior que  razao do subconjunto até agora
			sum_a += A[k];
			sum_b += B[k];
		i+=1
	rs = sum_a/sum_b;
	return rs


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
        print(subList)
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

def custom_pivot(ao,bo,A,B,K):
	a_sum = ao
	b_sum = bo
	for k in K:
		a_sum+=A[k[1]]
		b_sum+=B[k[1]]

	return a_sum/b_sum

"""
def rec_sol(ab,ini,end,firstA,firstB,A,B):
	if (ini > end ):
		return end
    if (ini == len(ab) -1):
        return end
    vec = []
    for k in range(ini,end):
        vec.append(k)
    pivot_med = median_of_medians(vet); # pega a mediana. O(n)
    pivot_local = my_partition(a_b[pivot_med].r,_i,_j); //iv: i e 1, j e o len de ab
"""

def optimaly_test(J1,J2,J3,ab,A,B,ao,bo,abk,X):
	a = ao
	b = bo
	print("J1:",J1)
	for j in J1:
		a+=A[j[1]] #pega os elementos de A que estao no set J
		b+=B[j[1]] #pega os elementos de B que estao no set J
	print('a:',a)
	print('b:',b)
	lamb = a/b
	print('ao',ao)
	print('bo',bo)

	print('lamb: ',lamb)
	
	if(lamb<abk):
		print('cond1')
		print('lamb<abk:',abk)
		print('J1: ',J1)
		for j in J1:
			X[j[1]] = 0
		J = J1
		

		rec_sol(J,ab,A,B,ao,bo,X)
	elif len(J3)>0:
		minj = 9999999
		for j in J3:
			if j[0]<minj:
				minj = j[0]

		ab1 = minj
		print('J3: ',J3)
		print(ab1)
		if(lamb>ab1):
			print('cond2')
			print('J2: ',J2)
			for j in J2:
				X[j[1]] = 1
			J = J2
			ao = a
			bo = b
			rec_sol(J,ab,A,B,ao,bo,X)
		else:
			J = []
			lamb_star = lamb
			d = {}

			#procedimento Set resultante tem que ter todos de J1, e nao ter os de J3
			for elem in J1:
				X[elem[1]] = 1

			if(len(J3)>0):
				for elem in J3:
					X[elem[1]] = 0
			
			#Ao/Bo are always in
			X[0] = 1
			print(X)
			print(lamb_star)
			a = 2/0
			return 0 #STOP

def custom_pivot(ao,bo,A,B,K):
	a_sum = ao
	b_sum = bo
	for k in K:
		#print('k:',k)
		a_sum+=A[k[1]]
		b_sum+=B[k[1]]

	return a_sum/b_sum

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

def partition(pivot,arr,low,high): 
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
	return ( i+1 ) 


def rec_sol(J,ini,end,ao,bo,A,B):
	print('rec_sol')
	print('J:',J)
	#pivot = median_of_medians(J[ini:end])# O(n)
	pivot = custom_pivot(ao,bo,A,B,J[ini:end])
	print('custom_pivot:',pivot)
	print('ini:',ini)
	print('end:',end)
	
	#pivot_local = my_partition(pivot,J,ini,end-1)
	pivot_local = partition(pivot,J,ini,end-1)
	print('pivot_local:',pivot_local)
	print(J)
	a = ao;
	b = bo;
	for k in range(pivot_local):
		a += A[J[k][1]]
		b += B[J[k][1]]
	rs = a/b
	r = J[pivot_local-1][0]

	#Trabalha so com metade, como na mochila
	if (r < rs):
		return rec_sol(J,ini,pivot_local-1,ao,bo,A,B);
	if (r > rs):
		return rec_sol(J,pivot_local+1,end,ao,bo,A,B);
	return end;

def algoritmo3(A,B):
	import sys
	sys.setrecursionlimit(10)
	ab = gera_ab(A,B)
	print('ab: ',ab)

	#rec_sol(ab,1,len(ab)-1,A[0],B[0],A,B)
	ao = A[0]
	bo = B[0]
	J = []
	#for i in range(1,len(ab)):
	#	if(A[i]/B[i]< ao/bo):
	#		J.append((A[i]/B[i],i)) #salve razoes e os indices deles
	J = ab
	print('J: ',J)
	#J sera o vetor das razoes onde se fara a busca recursiva. Sempre vai se descartar
	#metade dele, como na mochila
	pivot = rec_sol(J,0,len(J)-1,ao,bo,A,B)#J,ini,end,ab,A,B,ao,bo
	sum_a = ao
	sum_b = bo
	for k in range(1,pivot):
		a_k = A[J[k][1]]
		b_k = B[J[k][1]]
		r = (sum_a+a_k)/(sum_b + b_k)
		if (a_k/b_k > r):
			sum_a += A[J[k][1]];
			sum_b += B[J[k][1]];

	rs = sum_a/sum_b

	print('J: ',J)
	print(rs)





def main():
	from readpph import getData
	a,b,_,_,_ = getData()
	#a = [363,369,-376,131,-302,0]
	#b = [519, -153, -786, -162, 559, -53]
	print(sum(a)/sum(b))
	#
	# Instanciano a CPU timer  
	timer = CPUtimer.CPUTimer()
	print('Result of search: ')

	timer.reset()
	timer.start()
	#codigo
	alg1(a,b)
	#algoritmo1(a,b)
	#algoritmo3(a,b)
	#

	timer.stop()


main()
