import CPUtimer
from part import *
from mmedian import *


class AB():
	def __init__(self):
		self.ab_razao = []
		self.ab_ind = []

	def put(self,razao,ind):
		self.ab_razao.append(razao)
		self.ab_ind.append(ind) 
	
	def get_razao(self,ind):
		return ab_razao[ind]

def update(A,B,S):
	ao = A[0]
	bo = B[0]
	for i in range(1,len(S)):
		if(S[i]==1):
			ao+=A[i]
			bo+=B[i]
	return ao/bo

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
	while(1):#enquanto houver um elemento que caia num dos dois casos. O(n)
		cond = True #Enquanto houver alguem em S que satisfaz as 2 condicoes, o alg continua rodando
		
		
		for i in range(1,len(S)): # O(n)

			#Se tiver um cara fora de S que tiver razao maior que R*, entao ele tem que ser inserido 
			if S[i] == 0  and ab[i][0] > R_star: # O(1)
				
				S[i] = 1
				cond = False
				break
			#Se tiver um cara em S que tem razao menor que R*, entao ele tem que sair 
			elif S[i] == 1  and ab[i][0] < R_star: #nao satisfaz o lema
				
				S[i] = 0
				cond = False
				break
		if(cond):
			break
		R_star = update(A,B,S)

	#Ao fim do algoritmo, somente os valores otimos devem ficar em S, sendo assim o S*
	print('S: ',S)
	

def alg2(A,B):
	ab = gera_ab(A,B)
	J = []
	for x in range(len(ab)):
		J.append(0)

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
			J[i] = 1
		i+=1
	rs = sum_a/sum_b;	

	
	return rs

def custom_pivot(A,B,ini,end,J):
	a_sum = 0
	b_sum = 0 
	for k in range(0,end):
		
		a_sum+=A[J[k][1]]
		b_sum+=B[J[k][1]]
		
		#
		#

	return a_sum/b_sum

def rec_sol(J,ab,ini,end,ao,bo,A,B,l):
	if(ini > end ):
		
		return end
	if(ini == len(J)-1):

		return end
	
	
	if(l=='1'):
		slice_ab = ab[0:end]

		#pivot = median_of_medians(J[ini:end])# O(n)

		pivot = find_i_th_smallest( slice_ab,int((len(slice_ab) - 1) / 2))
		
		#pivot = pivot[0]
	elif(l=='2'):
		pivot = custom_pivot(A,B,ini,end,J)# O(n)
		
	
	
	
	pivot_local = my_partition(pivot,J,ini,end)
	
	
	#
	a = ao
	b = bo
	for k in range(ini,pivot_local+1):
		#
		a += A[J[k][1]]
		b += B[J[k][1]]
	
	rs = a/b
	r = A[J[pivot_local][1]] / B[J[pivot_local][1]]
	#r = J[pivot_local-1][0]
	

	#Trabalha so com metade, como na mochila
	
	if (r < rs):
		return rec_sol(J,ab,ini,pivot_local-1,ao,bo,A,B,l);
	if (r > rs):
		return rec_sol(J,ab,pivot_local+1,end,ao,bo,A,B,l);
	return end

def alg3(A,B,l = '1'):
	import sys
	sys.setrecursionlimit(100)
	J = []
	S = []

	J = gera_ab(A,B)
	ab = []
	for i in range(len(J)):
		ab.append(J[i][0])
	ao = A[0]
	bo = B[0]
	
	for i in range(0,len(ab)):
		S.append(0)
	
	#J sera o vetor das razoes onde se fara a busca recursiva. Sempre vai se descartar
	#metade dele, como na mochila
	pivot = rec_sol(J,ab,1,len(J)-1,ao,bo,A,B,l)#o ini deve comecar do 1(ao e bo n contam)
	
	sum_a = ao
	sum_b = bo
	J = J
	
	for k in range(1,pivot+1):
		a_k = A[J[k][1]]
		b_k = B[J[k][1]]
		r = (sum_a+a_k)/(sum_b + b_k)
		
		
		
		if (a_k/b_k > r):
			S[k] = 1
			sum_a += A[J[k][1]];
			sum_b += B[J[k][1]];
			

	print("S: ",S)
	rs = sum_a/sum_b


def main():
	#from readpph import getData
	#a,b,_,_,_ = getData()
	#a = [363,369,-376,131,-302,0]
	#b = [519, -153, -786, -162, 559, -53]
	#a = [1,4,8,1]
	#b = [3,2,4,5]
	a = [1,4,8,1,1,1,1,1]
	b = [3,2,4,5,5,5,5,5]
	
	
	#
	# Instanciano a CPU timer  
	timer = CPUtimer.CPUTimer()
	

	timer.reset()
	timer.start()
	#codigo
	alg1(a,b)
	#

	timer.stop()


main()
