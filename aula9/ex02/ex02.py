
#confere se um número é primo
def primo(n):
	i=2
	while i*i <= n: #confere só a até a raiz qdd de n
		if(n % i == 0):
			return False
		i += 1
	return True

#função confere as somas de dois números que somam n
#e ambos são primos
def soma_de_primos(n):
	for i in range(2,n//2+1):
		if(primo(i) and primo(n-i)):
			print("%d é a soma dos primos %d e %d"%(n,i,n-i))
			return
	print("%d não é soma de primos"%(n))

def main():
	n=int(input())
	for i in range(1, n+1): #confere a soma de todos número até n
		soma_de_primos(i)

main()