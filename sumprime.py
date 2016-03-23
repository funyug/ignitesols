i=2
sum=0
while i <= 1000:
	c=0
	k=1
	while k<i:
		if i%k==0:
			c=c+1
		k=k+1
	if c==1:
		sum=sum+i
	i=i+1
print sum