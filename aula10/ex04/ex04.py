
def main():
	n=int(input())
	l1=[]
	for i in range(n):
		l1.append(int(input()))

	m=int(input())
	l2=[]
	for i in range(m):
		l2.append(int(input()))
	
	lf=[]
	
	i=j=0
	while i < n or j < m:
		if j==m:
			lf.append(l1[i])
			i+=1
		elif i==n:
			lf.append(l2[j])
			j+=1
		elif l1[i]<l2[j]:
			lf.append(l1[i])
			i+=1
		elif l1[i]>l2[j]:
			lf.append(l2[j])
			j+=1
		else:
			lf.append(l1[i])
			i+=1
			j+=1

	for item in lf:
		print(item, end=" ")
	

main()