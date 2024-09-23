students = 5
lst = []
count = 0

for i in range(students):
    value = int(input('성적을 입력하시요: '))
    lst.append(value)
    
print(f'성적평균 = {sum(lst) / len(lst)}')
print(f'최대점수 = {max(lst)}')
print(f'최소점수 = {min(lst)}')

for score in lst:
    if score >= 80:
        count += 1
        
print(f'80점 이상 = {count}')