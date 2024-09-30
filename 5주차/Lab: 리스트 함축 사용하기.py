# 0부터 99까지의 정수 중 2의 배수이면서 3의 배수인 수들을 리스트로 만들기
result = [x for x in range(100) if x % 2 == 0 and x % 3 == 0]
print(result)
