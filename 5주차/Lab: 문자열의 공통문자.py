# ❑사용자로부터 2개의 문자열을 받아서 두 문자열의 공통문자를 출력하는 프로그램을 작성해보자.
str1 = input('첫번째 문자열: ')
str2 = input('두번째 문자열: ')

set1 = set(str1)
set2 = set(str2)

common_chars = set1 & set2


print('공통적인 글자: ', ''.join(common_chars))


# 중복되지 않은 단어의 개수 세기
txt = input('입력 테스트: ')
words = txt.split(' ')
unique = set(words)

print(f'사용된 단어의 개수 = {len(unique)}')
print(unique)