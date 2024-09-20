'''
def get_area(radius):
    area = 3.14 * radius ** 2
    return area

result = get_area(3)
print(f'반지름이 3인 원의 면적 = {result}')

def get_area(radius):
    area = 3.14 * radius ** 2
    return area

# 서로 다른 인수로 호출될 수 있다
result1 = get_area(3)
result2 = get_area(20)
print(f'반지름이 3인 원의 면적 = {result1}')
print(f'반지름이 3인 원의 면적 = {result2}')

def get_sum(start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum

# 1과 10이 getsum의 인수가 된다
x = get_sum(1, 10)

# 1과 20이 getsum의 인수가 된다
y = get_sum(1, 20)

def get_area(radius):
    if radius > 0:
        return 3.14 * radius ** 2 # radius가 음수일 때는 아무것도 반환 x
    else:
        return 0
'''

def sub():
    return 1, 2, 3

a, b, c = sub()
print(a, b, c)