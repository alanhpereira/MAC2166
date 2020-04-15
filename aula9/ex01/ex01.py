
#função para calcular o fatorial de um número a
def fatorial(a):
	fat = 1
	for i in range(2,a+1):
		fat*=i
	return fat

#função que calcula o binomial n escolhe k
def binomial(n,k):
	return fatorial(n)//(fatorial(k)*fatorial(n-k))

#imprime um triangulo de pascal com n linhas
def triangulo(n):
	for i in range(0,n):
		for j in range(0,i+1):
			print("%5d "%binomial(i,j),end="")
		print()

def main():
	n=int(input())
	triangulo(n)

main()