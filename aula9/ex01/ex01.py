
def fatorial(a):
	fat = 1
	for i in range(2,a+1):
		fat*=i
	return fat

def binomial(n,k):
	return fatorial(n)//(fatorial(k)*fatorial(n-k))

def triangulo(n):
	for i in range(0,n):
		for j in range(0,i+1):
			print(binomial(i,j),end=" ")
		print()

def main():
	n=int(input())
	triangulo(n)

main()