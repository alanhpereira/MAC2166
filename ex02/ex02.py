
def main() :
	n = int(input())
	i = int(input())
	j = int(input())
	mi=0		#multiplos de i
	mj=0		#multiplos de j
	cont = 0	#contagem de números multiplos de i ou j
	while cont<n:
		
		if mi < mj:
			print(mi)
			mi += i
		elif mj < mi:
			print(mj)
			mj += j
		else:	#caso nenhum dos dois forem menores que o outro, são iguais
			print(mi)
			mi += i
			mj += j
			
		cont +=1
main()