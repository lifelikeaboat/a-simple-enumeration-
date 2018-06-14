def main(start=1,sum=10,k=[]):
	if start==sum:
		yield k
	for start in list(range(1,sum+1)):
		if   (len(k)>0 and k[-1]>=start):
			continue
		for result in main(start=start+1,sum=sum,k=k+[start]):
			yield result
