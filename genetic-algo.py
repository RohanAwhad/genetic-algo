s = input("Enter any phrase: ")
import string
import random

choices = list(string.ascii_letters)
choices.append(' ')
choices.append('.')
n = len(s)
population = 1000
mutation_rate = 2

def initial_population():
	agents = []
	for i in range(population):	
		temp = ''
		for _ in range(n):
			temp += random.choice(choices)
		agents.append(temp)
		
	return agents
		
def calculate_fitness(agents):
	#if not agents: initial_population()
	fitness = []
	for i in range(population):
		correctness = 0
		for j in range(n):
			if agents[i][j] == s[j]: correctness += 1
		fitness.append([agents[i], correctness**2])
	#print(type(fitness[0][0]))
	return fitness

def calculate_probability(fitness):
	total_sum = 0
	bucket = []
	for i in range(len(fitness)):
		total_sum += fitness[i][1]
	#probability of each agent
	for i in range(len(fitness)):
		p = (fitness[i][1]/total_sum) * 10000
		bucket.extend([fitness[i][0] for _ in range(int(p))])
		
	#shuffle bucket
	random.shuffle(bucket)
	#print(type(bucket[0]))
	return bucket
	
def mutate(child):
	temp = ''
	for i in range(n):
		if random.randint(1,100) == mutation_rate:
			temp += random.choice(choices)
		else: temp += child[i]
		
	return temp

def mate(bucket):
	childs = []
	for _ in range(population):
		parents_array = []
		for x in range(2):
			parents_array.append(bucket[random.randint(0,len(bucket)-1)])
		#print(parents_array)
		i = 0
		temp = ''
		while i < n:
			t = random.randint(0,1)
			#print(type(parents_array[t]))
			temp += parents_array[t][i]
			i += 1 
		temp = mutate(temp)
		childs.append(temp)
		
	return childs
	
def check(fitness):
	for i in range(len(fitness)):
		if fitness[i][1] == n**2: return i
		
	return -1

	
	
def main():
	generations = 0	
	agents = []	
	while True:	
		if not agents: agents = initial_population()
		fitness = calculate_fitness(agents)
		index = check(fitness)
		if index != -1: 
			print('Your phrase was \"'+fitness[index][0]+'\"') 
			break
			
		else:
			mating_pool = calculate_probability(fitness)
			agents = mate(mating_pool)
			print('Generation:',generations)
			generations += 1
		
main()
