# sum recursion

def recursiveSum(arr):
	# print(arr)
	if len(arr) == 1:
		return arr[0]
	else:
		f = arr[0] + recursiveSum(arr[1:])
		return f

print(recursiveSum([1,2,3,4,5,6,7,8]))

#  factorial recursion

def factorial(n):
	if n<=1:
		return 1
	else:
		return n * factorial(n-1)

print(factorial(5))

# test = [1,2,3,4,5,6,7,8]
# print(test[1:])

# fibonacci number 
# fib(1) = fib(2) = 1
# fib(n) = fib(n-1) + fib(n-2)

# naive method

def fib(n):
	if n <=2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

print(fib(6))

# Memoized Dynamic programming alg

memo = {}
def fib2(n):
	if n in memo:                  # 1 => check if value is in memo table
		return memo[n]
	if n<=2:
		f = 1
	else:                          # 2 => continue with computations
		f = fib2(n-1) + fib2(n-2)
	memo[n] = f                    # 3 => save in memo table
	return f

print(fib2(6))




