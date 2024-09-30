'''
def create_acronym(sentence):
    # 문장을 단어별로 분리
    words = sentence.split()
    # 각 단어의 첫 글자를 추출하고 대문자로 변환
    acronym = ''.join(word[0].upper() for word in words if word)
    return acronym

# 사용자로부터 입력 받기
input_sentence = input("문자열을 입력하시오: ")
result = create_acronym(input_sentence)
print(result)
'''

pharse = input('문자열을 입력하시오: ')

acronym = ""

for word in pharse.upper().split():
    acronym += word[0]
    
print(acronym)