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
		print('S:',S)
		print('R_star:',R_star)
		for i in range(1,len(S)): # O(n)

			#Se tiver um cara fora de S que tiver razao maior que R*, entao ele tem que ser inserido 
			if S[i] == 0  and ab[i][0] > R_star: # O(1)
				print('ab[i][0]:',ab[i][0])
				S[i] = 1
				cond = False
				break
			#Se tiver um cara em S que tem razao menor que R*, entao ele tem que sair 
			elif S[i] == 1  and ab[i][0] < R_star: #nao satisfaz o lema
				print('ab[i][0]:',ab[i][0])
				S[i] = 0
				cond = False
				break
		if(cond):
			break
		R_star = update(A,B,S)

	#Ao fim do algoritmo, somente os valores otimos devem ficar em S, sendo assim o S*
	print('S_star: ',S)
	print('R_star: ',R_star)

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
	for k in range(i):
		print("[" ,ab[k][1] , ": " , A[ab[k][1]] , "," ,B[ab[k][1]] , ": " ,ab[k][0] ,"]")

	print(J)
	return rs

def custom_pivot(A,B,ini,end,J):
	a_sum = 0
	b_sum = 0 
	for k in range(0,end):
		print('k:',k)
		a_sum+=A[J[k][1]]
		b_sum+=B[J[k][1]]
		print(a_sum)
		#print('a:',A[J[k][1]])
		#print('b:',B[J[k][1]])

	return a_sum/b_sum

def rec_sol(J,ini,end,ao,bo,A,B,l):
	if(ini > end ):
		print('final')
		return end
	if(ini == len(J)-1):

		return end
	print('working with: ',end-ini)
	print('end:',end,' ini:',ini)
	if(l=='1'):
		K=[]
		for i in range(0,end):
			K.append(J[i][0])
		#pivot = median_of_medians(J[ini:end])# O(n)

		pivot = find_i_th_smallest( K,int((len(K) - 1) / 2))
		print('pivot med: ',pivot)
		#pivot = pivot[0]
	elif(l=='2'):
		pivot = custom_pivot(A,B,ini,end,J)# O(n)
		print('custom pivot: ',pivot)
	
	
	
	pivot_local = my_partition(pivot,J,ini,end)
	print('partitioned J:',J)
	print('pivot_local:',pivot_local)
	#print(J)
	a = ao
	b = bo
	for k in range(ini,pivot_local+1):
		#print('k:',k)
		a += A[J[k][1]]
		b += B[J[k][1]]
	print(a,b)
	rs = a/b
	r = A[J[pivot_local][1]] / B[J[pivot_local][1]]
	#r = J[pivot_local-1][0]
	print(J[pivot_local])

	#Trabalha so com metade, como na mochila
	print('r: ',r, ' rs: ',rs)
	if (r < rs):
		return rec_sol(J,ini,pivot_local-1,ao,bo,A,B,l);
	if (r > rs):
		return rec_sol(J,pivot_local+1,end,ao,bo,A,B,l);
	return end

def alg3(A,B,l = '1'):
	import sys
	sys.setrecursionlimit(100)
	ab = gera_ab(A,B)
	ao = A[0]
	bo = B[0]
	J = []
	S = []
	for i in range(0,len(ab)):
		S.append(0)
	#for i in range(1,len(ab)):
	#	if(A[i]/B[i]< ao/bo):
	#		J.append((A[i]/B[i],i)) #salve razoes e os indices deles
	J = ab
	print('J: ',J)
	#J sera o vetor das razoes onde se fara a busca recursiva. Sempre vai se descartar
	#metade dele, como na mochila
	pivot = rec_sol(J,1,len(J)-1,ao,bo,A,B,l)#o ini deve comecar do 1(ao e bo n contam)
	print('final pivot: ',pivot)
	sum_a = ao
	sum_b = bo
	print("[" ,ab[0][1] , ": " , A[ab[0][1]] , "," ,B[ab[0][1]] , ": " ,ab[0][0] ,"]")
	for k in range(1,pivot+1):
		a_k = A[J[k][1]]
		b_k = B[J[k][1]]
		r = (sum_a+a_k)/(sum_b + b_k)
		print('a_k: ',a_k)
		print('b_k: ',b_k)
		print(r)
		if (a_k/b_k > r):
			S[k] = 1
			sum_a += A[J[k][1]];
			sum_b += B[J[k][1]];
			print("[" ,ab[k][1] , ": " , A[ab[k][1]] , "," ,B[ab[k][1]] , ": " ,ab[k][0] ,"]")

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
	
	print(sum(a)/sum(b))
	#
	# Instanciano a CPU timer  
	timer = CPUtimer.CPUTimer()
	print('Result of search: ')

	timer.reset()
	timer.start()
	#codigo
	alg3(a,b,l='1')
	#

	timer.stop()


main()
