
def main():
	n=int(input())
	seq=[]
	for i in range(n):
		a=float(input())
		achou = False
		for e in seq:
			if a == e:
				achou=True
		if not achou:
			seq.append(a)
	
	for e in seq:
		print(e,end=" ")

main()