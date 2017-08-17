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