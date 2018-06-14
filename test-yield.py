def main(i=1,j=10,k=[]):
	if i==j:
		yield k
	for i in list(range(1,j+1)):
		if  i>j or (len(k)>0 and k[-1]>=i):
			continue
		for x in main(i=i+1,j=j,k=k+[i]):
			yield x
