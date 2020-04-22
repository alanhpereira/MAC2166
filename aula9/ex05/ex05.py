
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
	n=int(input())
	mdc_total=int(input()) #mdc cumulativo começa com o primeiro número da entrada
	for i in range(1,n):
		b=int(input())
		mdc_total=mdc(mdc_total,b)
	print("O mdc de todos os números é",mdc_total)

main()