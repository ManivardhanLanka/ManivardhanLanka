def s(x,y):
	x,y = y,x
	for i,j in Zip(x[::1],y[::-1]):
		print(i,j)
print(s('shalini','chandu'))