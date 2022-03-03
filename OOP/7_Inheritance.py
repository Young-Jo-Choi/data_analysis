"""
[클래스 상속]

1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.

2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.

3. 메서드 오버라이딩

4. super()

5. Python의 모든 클래스는 object 클래스를 상속한다. : 모든 것이 객체임

MyClass.mro() --> 상속관계를 보여준다.

(아래에 해당하는 주석에 번호를 매겨 예시를 삼음)
"""
# 지난 번과 같은 클래스(부모가 됨)
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


# 자식 클래스 - 1
class Siri_origin(Robot):
    pass


# 자식 클래스 - 2
class Siri(Robot):
    def __init__(self, name, age):  ##충돌 --> 덮어씌워짐 : 메서드 오버라이딩 - 3
        self.name = name
        self.age = age
        Siri.population += 1

    def call_me(self):
        print("네?")

    def cal_mul(self, a, b):
        return a * b

    @classmethod
    def hello_apple(cls):
        print(f"{cls} hello apple")

    # 오버라이딩 - 3 : 덮어씌워짐
    def say_hi(self):
        print(f"Greetings, my master call me {self.name}. by apple.")

    @classmethod  # classmethod 역시 오버라이딩 가능
    def how_many(cls):
        return f"We have {cls.population} robots. by apple"


# siri_origin = Siri_origin("siri")

# print(siri_origin)  # 부모의 __str__이 실행됨
# siri_origin.this_is_Robot_class()
# print(siri_origin.cal_add(17, 18))

siri = Siri("iphone8", 3)
siri.call_me()
print(siri.cal_mul(4, 3))
print(siri.cal_add(5, 8))
Siri.hello_apple()

print("오버라이딩")
siri.say_hi()
print(Siri.how_many())
