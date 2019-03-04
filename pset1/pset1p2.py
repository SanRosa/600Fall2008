import math

#First 1000 primes
prime_candidates = list(range(3,8000,2))
prime_counter = 0
prime_sum = 0

for candidate in prime_candidates:
	#Assume every number is prime
	is_prime = True
	for number in range(2, int(math.sqrt(candidate)) + 1):
		#If at some point is divisible then is not prime and you can exit the loop
		if(candidate % number == 0):
			is_prime = False
			break
	#At the end of the iteration check to add to prime number count
	if(is_prime):
		prime_counter += 1
		prime_sum += math.log(candidate)
	#Print the 1000th prime number(program did not check number 2 to see if it is prime)
	if(prime_counter == 999):
		print(candidate)
		print(prime_sum)
		break
