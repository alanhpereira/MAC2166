def main():
	n = int(input())
	if n >= 2:
		a1 = int(input())
		a2 = int(input())
		r = a2-a1
		ant = a2 # número anterior na PA
		pa=True
		for i in range(2,n):
			atual = int(input())
			if atual-ant!=r:
				pa=False
			ant=atual
		if(pa):
			print("É P.A.")
		else:
			print("Não é P.A.")
	else:
		print("É P.A.")
	
main()