
#calcula MDC usando algoritmo de euclides
def mdc(a,b):
	#não é necessário inverter a e b
	#caso b seja maior, pois o proprio 
	#algoritimo corrige sozinho
	while b>0:
		r=a%b
		a=b
		b=r
	return a

def main():
	a=int(input())
	b=int(input())
	print("O MDC é",mdc(a,b))

main()