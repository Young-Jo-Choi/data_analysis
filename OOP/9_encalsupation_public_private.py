"""
public vs private
"""


class Robot:

    # 클래스 변수 : 인스턴스들이 공유하는 변수
    population = 0

    def __init__(self, name, age):
        # self.__name = name  # private: 상속 역시 안된다.
        self.name = name
        self.age = age
        Robot.population += 1

    # 인스턴스 메서드
    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    # 인스턴스 메서드
    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):  # self는 인스턴스를 받고 cls는 클래스를 받는다.
        print(f"We have {cls.population} robots.")


# protect 개념
class Siri(Robot):
    def __init__(self, name, age):
        super().__init__(name, age)
        print(self.name)
        self.__age = 999
        print(self.__age)


ss = Robot("yss", 8)
print(ss.age)
ss.age = -999
print(ss.age)
"""
result : 
8
-999
보호가 안됐음 --> 내부적으로 접근할 수 없게 만드는 방법이 필요(private)
"""
# print(ss.__name)
# ss.name = "jack"
# print(ss.name)
"""
(위 세줄은 일부로 에러를 일으킫게 만들었으므로 일단 주석처리)
(에러를 보려면 Robot의 __init__에서 self.__name = name의 주석을 해제하시오. )
self.__name과 같이 하면 private -> 접근조차 안되게 막아버림(은닉) (__name__은 private 아님)
ss.name, ss.__name 둘다 ~has no attribute ~ 이런식의 에러메세지가 출력됨

클래스 내의 함수명이나 클래스 메서드, 클래스 변수 명 역시 __를 앞에 붙이면 private으로써 바깥에서 접근 불가
"""

# protect개념
ssss = Siri("iphone8", 9)
# print(ssss.__age)  # --> 에러 : private이므로 바깥에서 실행 불가
