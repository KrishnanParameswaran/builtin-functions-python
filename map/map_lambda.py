# By Krishnan Parameswaran

# Double the given number

def multiplication(n):
    return 2*n

nums = [10, 100, 1000, 10000]

result1 = map(multiplication, nums)
print(result1)
print("Double the list of numbers using map")
print(list(result1))

print("Double the list of numbers using map and lambda")
result2 = map(lambda n : n+n, nums)
print(list(result2))

print("Element-wise addition of two lists")
num1 = [1, 2, 3, 4]
num2 = [5, 6, 7, 8]
result3 = map(lambda i,j : i+j, num1, num2)
print(list(result3))

print("Listify all strings in a list individually")
strings = ['HAVE', 'A', 'GREAT', 'DAY']
result4 = map(list, strings) 
print(list(result4))