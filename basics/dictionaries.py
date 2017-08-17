def fib(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fib(n-1)+fib(n-2)
print fib(4)

def sort(list):
	ref=list[0]
	for j in range(1,len(list)):
		for i in range (1,len(list)):
			if list[i]<list[i-1]:
				ref=list[i]
				list[i]=list[i-1]
				list[i-1]=ref
	return list


print(sort([5,4,3,2,1]))

def lists(a,b):
	c=a[1:]
	print('1 2 3 4 5')
	print(c)
	c=a[:2]
	print('0 1')
	print(c)
	c=a[1:4]
	print('1 2 3')
	print(c)
	c=a[:3]+a[3:]
	print('0 1 2 3 4 5')
	print(c)

lists([0,1,2,3,4,5],[])
# Works as intended.

def dics(d):
	