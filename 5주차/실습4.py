'''
squares = []

for x in range(10):
    squares.append(x * x)
    
squares = [ x * x for x in range(10) ]

prices = [135, -545, 922, 356, -992, 217]
mprices = [i if i > 0 else 0 for i in prices]
print(mprices)

words = ['All', 'good', 'things', 'must', 'come', 'to', 'an', 'end.']
letters = [w[0] for w in words]
print(letters)

numbers = [x + y for x in ['a', 'b', 'c'] for y in ['x', 'y', 'z']]
print(numbers)


fruits = ['apple', 'banana', 'grape']
for index, value in enumerate(fruits):
    print(index, value)
    

numbers = set([1,2,3,1,2,3])
print(numbers)

letters = set('abc')
print(letters)

fruits = {'apple', 'banana', 'grape'}
for x in fruits:
    print(x, end=' ')
    
fruits = {'apple', 'banana', 'grape'}
for x in sorted(fruits):
    print(x, end=' ')
    
# 딕셔너리_이름 = {키1: 값1, 키2: 값2, 키3: 값3, ...}

s = "Welcome to Python"
print(s.split())

s = "Hello, World!"
print(s.split(","))

s = "Hello, World!"
print(s.split(", "))

print(list("Hello, World!"))

'''


print(",".join(["apple", "grape", "banana"]))

print("-".join("010.1234.5678".split(".")))
