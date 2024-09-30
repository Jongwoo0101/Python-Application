# 원래 리스트
original_list = [10, 20, 30, 40, 50]

# 새로운 리스트: 0번째부터 i번째까지의 합계 계산
new_list = [sum(original_list[:i+1]) for i in range(len(original_list))]

# 결과 출력
print("원래 리스트:", original_list)
print("새로운 리스트:", new_list)
