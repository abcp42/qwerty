import CPUtimer

#teste se o frasco quebrou nesse intervalo entre potências
def testJar(step,goal_level):
	print('step: ',step,', goal: ',goal_level)
	if(step >= goal_level):
		print('True!')
		return True
	return False


def lineSearch(n,step,goal_level):
	print(step)
	print(goal_level)
	#busque ate n
	while(step<n): 
		if(step == goal_level):
			print("True!")
			return True
		step+=1
	return False



 #k The number of jars available to you
 #n The size of the ladder
 #s From what rung you will begin your test on (assume the steps are 0-indexed)
def search2(n,s,goal_level):


	#step_size <- n^((k - 1)/k)
	step = s**2
	if(testJar(step,goal_level)):
		return lineSearch(n,(s-1)**2,goal_level)#busca linear a partir do intervalo anterior

	s+=1
	return search2(n,s,goal_level)


def search3(n,s,goal_level):

	#step_size <- n^((k - 1)/k)
	step = s**3
	if(testJar(step,goal_level)):
		print('Search 2')
		return search2(n,(s-1), goal_level)

	s+=1
	return search3(n,s,goal_level)

def search4(n,s,goal_level):

	#step_size <- n^((k - 1)/k)
	step = s**4
	if(testJar(step,goal_level)):
		print('Search 3')
		return search3(n,(s-1), goal_level)

	s+=1
	return search4(n,s,goal_level)


def searchk(k,n,s,goal_level):

	#step_size <- n^((k - 1)/k)
	#step = s**3
	step = s**(k)
	if(testJar(step,goal_level)):
		print('Search: ',k)
		print('Search in Step: ',s-1)
		if(k==2):
			print('Search 2!')
			return search2(n,(s-1), goal_level)
		else:
			return searchk(k-1,n,(s-1), goal_level)

		#return lineSearch((s-1)**3,n,goal_level)#busca linear a partir do intervalo anterior

	s+=1
	return searchk(k,n,s,goal_level)

def main():
	a=0
	decimal = 0
	maxval = 0
	with open("bignum_32_01.dat", "rb") as text_file:
		# One option is to call readline() explicitly
		# single_line = text_file.readline()

		# It is easier to use a for loop to iterate each line
		for line in text_file:
			a+=1
			if(a==1):
				print('Max value: ')
				maxval = (2**int(line[0:2]))-1
				print(maxval)
				continue
			if(int(line,2)>maxval):
				print('error')
				break
			print(int(line,2))
		search2(2,maxval,)

# Instanciano a CPU timer  
timer = CPUtimer.CPUTimer()
print('Result of search: ')

timer.reset()
timer.start()
#r =search2(3476,1,1567)
#r =search2(4294967296,1,3534967296)
#r =search4(500,1,100)
searchk(32,50000000,1,33445543) #Erro too many rec
#print(searchk(5,500000,1,334455)) 
timer.stop()
# Imprimindo resultados de diversas formas
print("Tempo Total: " + str( timer.get_time() ) +" s")
print("Tempo Medio: " + str( timer.get_time("average","micro") ) +" \u00B5s")
print("Ultima Chamada: " + str( timer.get_time("last","micro") ) +" \u00B5s")
print("Estampa 1 do total: " + str( timer.get_stamp("total","si") ) ) 
print("Estampa 2 do total: " + str( timer.get_stamp("total","clock") ) )


################ Line Search ################
"""
timer.reset()
timer.start()
print(lineSearch(500000,1,334455))
timer.stop()
# Imprimindo resultados de diversas formas
print("Tempo Total: " + str( timer.get_time() ) +" s")
print("Tempo Medio: " + str( timer.get_time("average","micro") ) +" \u00B5s")
print("Ultima Chamada: " + str( timer.get_time("last","micro") ) +" \u00B5s")
print("Estampa 1 do total: " + str( timer.get_stamp("total","si") ) ) 
print("Estampa 2 do total: " + str( timer.get_stamp("total","clock") ) )
"""


