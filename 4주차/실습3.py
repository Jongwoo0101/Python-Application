'''
temps = [28, 31, 33, 35, 27, 26, 25]

for i in range(len(temps)):
    print(temps[i], end=', ')
    
questions = ['name', 'quest', 'color']
answers = ['Kim', '파이썬', 'blue']
for q, a in zip(questions, answers):
    print(f'What is your {q}? It is {a}')
    

heros = []
heros.append('아이언맨')
heros.append('토르')

heros = ['아이언맨', '토르', '헐크']
heros.insert(1, '스파이더맨')
print(heros)


heros = ['아이언맨', '토르', '헐크', '스칼렛 위치', '헐크']

n = heros.index('헐크')

heros = ['아이언맨', '토르', '헐크']
heros.pop(1)
print(heros)

heros = ['아이언맨', '토르', '헐크']

if '토르' in heros:
    heros.remove('토르')
    

numbers = [10, 20, 30, 40, 50]

print('합 = ', sum(numbers))
print('최대값 = ', max(numbers))
print('최소값 = ', min(numbers))


import random

numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('랜덤하게 선택한 항목 = ', random.choice(numberList))

temps = [28, 31, 33, 35, 27, 26, 25]
values = temps

print(temps) # temps 리스트 출력
values[3] = 39 # values 리스트 변경
print(temps) # temps 리스트가 변경되었다.


temps = [28, 31, 33, 35, 27, 26, 25]
values = list(temps) # list()는 리스트 객체의 생성자임, 객체를 생성하고 초기화하는 함수임. 다른 객체들을 받아서 리스트로 변환함

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
sublist = numbers[2:7]
print(sublist)

print(numbers[:3])
print(numbers[3:])
print(numbers[:])

lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst[0:3] = ['white', 'blue', 'red']
print(lst)

lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst[::2] = [99, 99, 99, 99]
print(lst)

lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst[:] = []
print(lst)

numbers = list(range(0, 10)) # 0에서 시작하여 9까지를 저장하는 리스트
print(numbers)
del numbers[-1]
print(numbers)

'''

s = 'Monty Python'
print(s[0])
print(s[6:10])
print(s[-12:-7])