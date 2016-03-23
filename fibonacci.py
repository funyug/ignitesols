a, b = 1, 2
total = 0
sum=0
while a <= 4000000:
	if a % 2 == 0:
		sum=sum+a
	a, b = b, a+b
print sum