
def main():
	lanc=[]
	for i in range(37):
		lanc.append(0)

	n=int(input())
	for i in range(n):
		idx = int(input())
		lanc[idx]+=1
	
	for i in range(37):
		print("frequencia de %d é %d"%(i,lanc[i]))

main()