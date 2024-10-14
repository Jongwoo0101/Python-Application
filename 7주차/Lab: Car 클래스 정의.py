class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model
        
    def drive(self):
        self.speed = 60
        
myCar = Car(0, "blue", "S-Class")

print('자동차 객체를 생성하였습니다.')
print(f'자동차의 속도는 {myCar.speed}')
print(f'자동차의 색상은 {myCar.color}')
print(f'자동차의 모델은 {myCar.model}')

myCar.drive()
print(f'자동차의 속도는 {myCar.speed}')