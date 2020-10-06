#Contributed by rockysaikia730

def gcd(x,y):
	i=2
	while i<=x and i<=y:
		if ((x%i == 0) and (y%i == 0)):
			gcd = i
			break
		i += 1
	else:
		gcd = 1
	return gcd
