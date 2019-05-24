import CPUtimer

#teste se o frasco quebrou nesse intervalo entre potências
def testJar(step,goal_level):
	#print('step: ',step,', goal: ',goal_level)
	if(step >= goal_level):
		print('True!')
		print("step is now: ",step)
		return True
	return False


def lineSearch(step,n,goal_level,accumulated_positions):
	print(step)
	print(goal_level)
	#busque ate n
	while(step<n): 
		if(step == goal_level):
			print("Found it!")
			print("Floor is: ",accumulated_positions+step)
			return True
		step+=1
	print("Did not find it...")
	return False



 #k The number of jars available to you
 #n The size of the ladder
 #s From what rung you will begin your test on (assume the steps are 0-indexed)
 #begin_step: the begin of the interval of numbers you have to search for
 #end_step: the end of the interval of numbers you have to search for

def search2(goal_level,begin_step,end_step,accumulated_positions):
	last_step = 0
	while(1):
		#step_size <- n^((k - 1)/k)
		step = begin_step**2
		if(testJar(step,goal_level)):
			#normalize interval
			return lineSearch(last_step,end_step,goal_level,accumulated_positions)#busca linear a partir do intervalo anterior
		last_step = step
		begin_step+=1
	#return search2(goal_level,begin_step,end_step,accumulated_positions)
	return

def search3(goal_level,begin_step,end_step,accumulated_positions):
	last_step = 0
	#step_size <- n^((k - 1)/k)
	while(1):
		step = begin_step**3
		if(testJar(step,goal_level)):
			print('Search 2')

			#it has to search on the interval (c-1)n^(1/k) to cn^(1/k) normalized to 0-1 
			end_step = step - (begin_step-1)**3 
			goal_level = goal_level - (begin_step-1)**3 #have to translate goal to new interval
			accumulated_positions+= (begin_step-1)**3 #go saving to remember the true floor/ goal
			print("new interval: from 1 to ",end_step)
			return search2(goal_level,1,end_step,accumulated_positions)

		begin_step+=1
		#return search3(goal_level,begin_step,end_step,accumulated_positions)
	return


def search4(goal_level,begin_step,end_step,accumulated_positions):
	last_step = 0
	#step_size <- n^((k - 1)/k)
	while(1):
		step = begin_step**4
		if(testJar(step,goal_level)):
			print('Search 3')

			#it has to search on the interval (c-1)n^(1/k) to cn^(1/k) normalized to 0-1 
			end_step = step - (begin_step-1)**4
			goal_level = goal_level - (begin_step-1)**4 #have to translate goal to new interval
			accumulated_positions+= (begin_step-1)**4 #go saving to remember the true floor/ goal
			print("new interval: from 1 to ",end_step)
			return search3(goal_level,1,end_step,accumulated_positions)

		begin_step+=1
		#return search3(goal_level,begin_step,end_step,accumulated_positions)
	return

def searchk(k,goal_level,begin_step,end_step,accumulated_positions):

	#step_size <- n^((k - 1)/k)
	step = begin_step**(k)
	if(testJar(step,goal_level)):
		print('Search: ',k)
		#it has to search on the interval (c-1)n^(1/k) to cn^(1/k) normalized to 0-1 
		end_step = step - (begin_step-1)**k
		goal_level = goal_level - (begin_step-1)**k #have to translate goal to new interval
		accumulated_positions+= (begin_step-1)**k #go saving to remember the true floor/ goal
		print("new interval: from 1 to ",end_step)
		print('accumulated_positions: ',accumulated_positions)
		if(k==2):
			print('Search 2!')
			return search2(goal_level,1,end_step,accumulated_positions)
		else:
			return searchk(k-1,goal_level,1,end_step,accumulated_positions)
	begin_step+=1
	return searchk(k,goal_level,begin_step,end_step,accumulated_positions)

def searchkk(k,goal_level,begin_step,end_step,accumulated_positions):

	last_step = 0
	#step_size <- n^((k - 1)/k)
	while(1):
		#step_size <- n^((k - 1)/k)
		step = begin_step**(k)
		if(testJar(step,goal_level)):
			print('Search: ',k)
			#it has to search on the interval (c-1)n^(1/k) to cn^(1/k) normalized to 0-1 
			end_step = step - (begin_step-1)**k
			goal_level = goal_level - (begin_step-1)**k #have to translate goal to new interval
			accumulated_positions+= (begin_step-1)**k #go saving to remember the true floor/ goal
			print("new interval: from 1 to ",end_step)
			print('accumulated_positions: ',accumulated_positions)
			if(k==2):
				print('Search 2!')
				return search2(goal_level,1,end_step,accumulated_positions)
			else:
				return searchk(k-1,goal_level,1,end_step,accumulated_positions)
		last_step = step
		begin_step+=1
	return 
def getTests(filename):
	a=0
	decimal = 0
	maxval = 0
	tests = []
	with open(filename, "rb") as text_file:
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
			#if(int(line,2)>maxval):
			#	print('error')
			#	break
			tests.append(int(line,2))
			print(int(line,2))
	return tests,maxval

#tests,maxval = getTests("bignum_32_01.dat")
tests,maxval = getTests("bignum_64_01.dat")
#tests,maxval = getTests("bignum_128_01.dat")
#tests,maxval = getTests("bignum_192_01.dat")
#tests,maxval = getTests("bignum_256_01.dat")
print('Max value: ',maxval)

import sys
sys.setrecursionlimit(100000)

# Instanciano a CPU timer  
timer = CPUtimer.CPUTimer()
print('Result of search: ')

timer.reset()
timer.start()
#searchk(4,1567,1,3476,0) #Erro too many rec


#search22(tests[0] ,1,maxval,0)
#search33(tests[0] ,1,maxval,0)
#search4(tests[0] ,1,maxval,0)
searchk(6,tests[0],1,maxval,0)
timer.stop()
# Imprimindo resultados de diversas formas
print("Tempo Total: " + str( timer.get_time() ) +" s")
print("Tempo Medio: " + str( timer.get_time("average","micro") ) +" \u00B5s")
print("Ultima Chamada: " + str( timer.get_time("last","micro") ) +" \u00B5s")
print("Estampa 1 do total: " + str( timer.get_stamp("total","si") ) ) 
print("Estampa 2 do total: " + str( timer.get_stamp("total","clock") ) )



timer.reset()
timer.start()
#lineSearch(1,50000000,33445500,0)
timer.stop()
# Imprimindo resultados de diversas formas
print("Tempo Total: " + str( timer.get_time() ) +" s")
print("Tempo Medio: " + str( timer.get_time("average","micro") ) +" \u00B5s")
print("Ultima Chamada: " + str( timer.get_time("last","micro") ) +" \u00B5s")
print("Estampa 1 do total: " + str( timer.get_stamp("total","si") ) ) 
print("Estampa 2 do total: " + str( timer.get_stamp("total","clock") ) )



