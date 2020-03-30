
def main() :
	n = int(input())
	i = int(input())
	j = int(input())
	atual = 0
	cont = 0
	while cont<n:
		if atual % i == 0 or atual % j == 0:
			print(atual)
			cont = cont + 1
		atual = atual + 1

main()