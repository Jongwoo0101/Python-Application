fact = 1

n = int(input("정수를 입력하시오: "))

for i in range(1, n+1):
    fact = fact * i  
    print(i, "!은", fact, "이다.")
    