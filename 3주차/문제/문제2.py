def coffee(c):
    if c == 'Americano':
        return 3900
    
    elif c == 'Cafe mocha':
        return 45000
    
    elif c == 'Cafe Latte':
        return 50000
    
    elif c == 'Green Tea':
        return 55000
    
    
def size(s):
    if s == 'G' or s == 'grande':
        return 1000
    
    elif s == 'R' or s == 'regular':
        return 500
    
    elif s == 'S' or s == 'short':
        return 0
    
def price(a, b):
    return a + b
    

print('Welcome to Harry Cafe')
c = input('Choose 1: Americano / Cafe mocha / Cafe Latte / Green Tea Latte : ')
s = input('Choose size: G(grande) / R(regular) / S(short) : ')

print(f'총 금액은 {price(coffee(c), size(s))}원 입니다.')