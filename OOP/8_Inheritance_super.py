"""
4. super()

5. Python의 모든 클래스는 object 클래스를 상속한다. : 모든 것이 객체임

MyClass.mro() --> 상속관계를 보여준다.
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

    def __init__(self, name):
        self.name = name  # 인스턴스 변수
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

    # magic method를 바꿈
    def __str__(self):
        return f"{self.name} Good Robot!"

    def __call__(self):
        print("Call")
        return f"{self.name} call!!"


# 자식 클래스 - 1
class Siri_origin(Robot):
    pass


# 자식 클래스 - 2
class Siri(Robot):
    def __init__(self, name, age):  ##충돌 --> 덮어씌워짐 : 메서드 오버라이딩 - 3

        # super는 부모객체(Robot)를 가리킨다. super는 __init__외에도 사용 가능, 아래에 예시 있음
        super().__init__(name)  # 부모객체의 __init__을 실행
        # Siri.population += 1 역시 필요 없음
        self.age = age

    def call_me(self):
        print("네?")

    def cal_mul(self, a, b):
        return a * b

    def cal_flexible(self, a, b):
        # 오버라이딩을 했기 때문에 자식클래스의 say_hi와는 다른 부모클래스의 say_hi가 나올 것
        super().say_hi()
        # 오버라이딩을 하지 않았으므로 cal_add를 self에서도 동일하게 사용가능
        return self.cal_mul(a, b) + self.cal_add(a, b) + super().cal_add(a, b)

    @classmethod
    def hello_apple(cls):
        print(f"{cls} hello apple")

    # 오버라이딩 - 3 : 덮어씌워짐
    def say_hi(self):
        print(f"Greetings, my master call me {self.name}. by apple.")

    @classmethod  # classmethod 역시 오버라이딩 가능
    def how_many(cls):
        return f"We have {cls.population} robots. by apple"


# 4- super를 이해하기 위함
siri = Siri("iphone8", 17)

print(siri.age)
print(siri.name)
siri.say_hi()
print(Siri.how_many())
print(siri.cal_flexible(1, 3))

# 5-모든 것은 객체임을 이해하기 위함
print(
    Siri.mro()
)  # [<class '__main__.Siri'>, <class '__main__.Robot'>, <class 'object'>]
print(Robot.mro())  # [<class '__main__.Robot'>, <class 'object'>]
"""
사실 class Robot(object): 에서 (object)가 생략된 것임
"""
print(int.mro())

""" 
다중 상속, 단 의미 없이 다중 상속을 쓰는 것은 안티 패턴
"""


class A:
    pass


class B:
    pass


class C:
    pass


# 이런 식으로 부품화가 가능
class D(A, B, C):
    pass
