"""
Para qualquer n n**3 é a soma de n impares consecutivos
com o primeiro sendo n**2 - n + 1
Prova:
soma dos n impares: 
n*(a₁+aₙ)/2
n*( (n**2 - n + 1) + (n**2 - n + 1 + 2(n-1) ) )/2
n*( 2(n**2) - n + 1 - n + 1 + 2n -2 )/2
n*( 2(n**2))/2
n**3
"""

def main():
	m = int(input())
	for n in range(1,m+1):
		a1=n*n - n + 1 #a1
		print(n**3,end=" = ")
		for i in range(n-1):
			print((a1+2*i),end=" + ") #gera PA
		print(a1+2*n) #An


main()