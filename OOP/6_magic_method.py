"""
__~~__ 형태의 magic method

살필 것
- __str__
- callable : 호출 가능한, 괄호()를 덧붙임. 함수형태에서 주로 이러고 인스턴스 변수는 not callable
"""


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
        print(f"Greetinhs, my masters call me {self.name}.")

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

    # magic method를 바꿈
    def __str__(self):
        return f"{self.name} Good Robot!"

    def __call__(self):
        print("Call")
        return f"{self.name} call!!"


droid1 = Robot("R2-D2", 1231132)
droid1.say_hi()

print(dir(droid1))
print(droid1)  ## def __str__ 한 것과 안한 것 비교
# print(droid1.__str__)

# 원래 객체는 callable하지 않기 때문에 다음과 같이 ()가 붙으면 에러가 난다.
# __call__  magic method를 수정함으로써 객체가 함수와 같은 callable 객체가 됨 :
#  call이라는 magic method가 정의되어 그런 것임
# 사실 함수 역시 객체이고 어떤 클래스로 만들어지는데 그 클래스에 __call__이 정의되어있는 것임
print(droid1())
