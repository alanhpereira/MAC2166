
def main():
	n=int(input())
	seq = []
	for i in range(n):
		seq.append(float(input()))
	for i in range(n-1,-1,-1):
		print("%.3f"%seq[i],end=" ")
	print()

main()