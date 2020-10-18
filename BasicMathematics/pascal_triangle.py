import math
def c(n, r):
	return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
def col(n):
	if n==1:
		return 1
	else:
		return n+1
row=int(input("rows:  "))
for i in range(1, row+1):
	print(end= " "*(row-i))
	for j in range (col(i)):
		print(int(c(i, j)), end=" ")
	print("")
