def lcm(a,b):
	if b > a :
		for i in range(1,a+1):
			num = b*i          
			if num % a == 0: # Checks if any multiple of the larger number is exactly divisible by the smaller number
				lcm = num
				break
			else:
				lcm = b*a	
		return(lcm)		

	if a > b:
		for i in range(1,b+1):
			num = a*i
			if num % b == 0:
				lcm = num
				break
			else:
				lcm = b*a
		return(lcm)
					
	if a == b :
		return(a) 				

print(lcm(13,12))		