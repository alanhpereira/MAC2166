
def main():
	n=int(input())

	mdc_total=int(input()) #MDC acumulativo

	for i in range(1,n):
		a=int(input())
		b=mdc_total
	
		while(b!=0): #faz o mdc entre a e o mdc acumulativo
			r = a%b
			a=b
			b=r
		
		mdc_total=a

	print(mdc_total)

main()