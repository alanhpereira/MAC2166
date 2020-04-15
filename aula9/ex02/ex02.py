
def primo(n):
	i=2
	while i*i <= n:
		if(n % i == 0):
			return False
		i += 1
	return True

def soma_de_primos(n):
	for i in range(2,n//2+1):
		if(primo(i) and primo(n-i)):
			print("%d é a soma dos primos %d e %d"%(n,i,n-i))
			return
	print("%d não é soma de primos"%(n))

def main():
	n=int(input())
	for i in range(1, n+1):
		soma_de_primos(i)

main()