'''
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
        
p = Point()
q = Point()

print(p.x, p.y, q.x, q.y)
print(p.__doc__) # 인스턴스의 클래스를 설명
print(p.__class__) # 객체 p의 클래스명 확인
print(p.__module__) # 클래스에 정의된 모듈
print(p.__dict__) # 인스턴스 p의 속성 값 정보

class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def setName(self, name):
        self.__name = name
        
    def getName(self):
        return self.__name
    
    def setAge(self, age):
        self.__age = age
        
    def getAge(self):
        return self.__age
    
missy = Cat('Missy', 3)
lucky = Cat('Lucky', 5)

print(missy.getName(), missy.getAge())
print(lucky.getName(), lucky.getAge())
'''


class Triangle():
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        
    numberOfSides = 3
    def checkAngles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        
        else:
            return False
        
triangle = Triangle(90, 30, 60)
print(triangle.checkAngles())