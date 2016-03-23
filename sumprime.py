num=raw_input("Enter a value:")
i=2
sum=0
while i <= int(num):
	c=0
	k=1
	while k<=i/2:
		if i%k==0:
			c=c+1
		k=k+1
	if c==1:
		sum=sum+i
	i=i+1
print sum