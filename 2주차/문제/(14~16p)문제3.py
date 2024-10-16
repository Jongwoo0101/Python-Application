import random

n = int(input('선택하시오(1: 가위 2: 바위 3: 보): '))
b = random.randint(1, 3)
print(f'컴퓨터의 선택(1: 가위 2: 바위 3: 보): {b}')

if n == b:
    print('비겼음!')
elif (n == 1 and b == 3) or (n == 2 and b == 1) or (n == 3 and b == 2):
    print('사용자 승!')
else:
    print('컴퓨터 승!')
