""" 
추상화 : 불필요한 정보는 숨기고 필요한 정보만을 표현함으로써
공통의 속성이나 행위(methods)를 하나로 묶어 이름을 붙임

namespace : 개체를 구분할 수 있는 범위
__dict__ : 네임스페이스를 확인할 수 있다.
dir() : 네임스페이스의 key값을 확인할 수 있다. 
(__dict__는 물리적으로 저장된 것들, dir()은 실제 사용가능한 것들)
__doc__ : class의 주석을 확인한다.
__class__ :  어떤 클래스로 만들어진 인스턴스인지 확인할 수 있다."""

# 클래스 변수와 클래스 메서드에 주목


class Robot:

    """
    __doc__을 확인하기 위한 주석임
    저자 : 최
    직위 : 사원
    거주지 : 군포
    """

    # 클래스 변수 : 인스턴스들이 공유하는 변수
    population = 0

    def __init__(self, name, code):
        self.name = name  # 인스턴스 변수
        self.code = code  # 인스턴스 변수
        Robot.population += 1

    # 인스턴스 메서드
    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    # 인스턴스 메서드
    def cal_add(self, a, b):
        return a + b

    # 인스턴스 메서드
    def die(self):
        print(f"{self.name} is being destroyed")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one")
        else:
            print(f"There are still {Robot.population} robots working.")

    @classmethod
    def how_many(cls):  # self는 인스턴스를 받고 cls는 클래스를 받는다.
        print(f"We have {cls.population} robots.")

    # static method : self나 cls 필요없음, 인스턴스 메서드로 접근 가능
    @staticmethod
    def this_is_Robot_class():
        print("Yes!!")


# 각각의 인스턴스는 독립적이지만 공통적으로 공유하는 클래스 변수라는 속성 존재
print(Robot.population)

siri = Robot("siri", 21020444)
print(Robot.population)
print(siri.name)

jarvis = Robot("jarvis", 4411221)
print(Robot.population)
print(jarvis.code)
print(jarvis.cal_add(4, 3))

Robot.how_many()

# 아래 두개는 똑같음
# say_hi는 인스턴스 메서드이지만 메모리 효율을 위해
# 클래스의 네임스페이스(Robot.__dict__)에 저장되어있음
Robot.say_hi(siri)
siri.say_hi()

print(Robot.__doc__)
print(siri.__class__)

Robot.this_is_Robot_class()
