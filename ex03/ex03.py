

def main() :
	n = int(input())
	i = 2	#inteiro para tentar divisão
	while n>1:
		if n % i == 0:
			cont = 0 #contador de multiplicidade
			while n % i == 0: #enquanto for divisivel
				cont += 1
				n = n // i
			print("fator %d muliplicidade %d"%(i,cont))
		i+=1 #aumenta o divisor

main()