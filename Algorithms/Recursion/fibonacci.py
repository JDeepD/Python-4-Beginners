#I used swapping technique, so that it does the memory work itself. I am writing a shorter approach to nth term of fibonacci

def fibonacci(n):
	a,b=0,1 #base is assumed as 0 and 1, so 0,1 and 1 are the 1st, 2nd and 3rd term respectively.
	for i in range(n-1):
		a,b=b,a+b
	return a
n=int(input("Enter n:  "))
print(fibonacci(n))
