
def main() :
	n = int(input())
	i = int(input())
	j = int(input())
	atual = 0	#número para conferir multilicipidade
	cont = 0	#contagem de números multiplos de i ou j
	while cont<n:
		if atual % i == 0 or atual % j == 0:
			print(atual)
			cont = cont + 1
		atual = atual + 1

main()