"""
다형성(polymorphism)
- 여러 형태를 가질 수 있도록 한다. 즉 객체를 부품화할 수 있도록 한다.
- 같은 형태의 코드가 다른 동작을 하도록 하는 것

composition
- 다른 클래스의 일부 메서드를 사용하고 싶지만, 상속은 하고 싶지 않은 경우
- 1. 부모 클래스가 변하면 자식 클래스는 계속 수정되어야 한다.
- 2. 부모 클래스의 메서드를 오버라이딩 하는 경우 내부 구현 방식의 얕은 이해로 오류가 생길 가능성 증가
"""


class Robot:

    __population = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Robot.__population += 1

    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return f"kim {self.__name}"

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise TypeError("invalid age")
        else:
            self.__age = new_age

    def __say_hi(self):
        print(f"Greetinhs, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):

        print(f"We have {cls.__population} robots.")


# 다형성
class Siri(Robot):
    def say_apple(self):
        print("hello my apple")


class Siriko(Robot):
    def say_apple(self):
        print("안녕하세요")


class Bixby(Robot):
    def say_samsung(self):
        print("안녕하세요")


# composition : 상속 없이 다른 클래스의 메서드 가져왔음
class BixbyCal:
    def __init__(self, name, age):
        self.Robot = Robot(name, age)

    def cal_add(self, a, b):
        return self.Robot.cal_add(a, b)
