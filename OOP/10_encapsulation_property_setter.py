"""
[property]
- 인스턴스 변수 값을 사용해서 적절한 값으로 보내고 싶을 때
- 인스턴스 변수 값에 대한 유효성 검사 및 수정
"""


class Robot:

    __population = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Robot.__population += 1

    # 1.
    # age 변수를 바깥에서 읽고는 싶은데 쓰기나 업데이트는 막고자 할 때
    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return f"kim {self.__name}"

    # 2.
    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise TypeError("invalid age")
        else:
            self.__age = new_age

    def __say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    # 인스턴스 메서드
    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):  # self는 인스턴스를 받고 cls는 클래스를 받는다.
        print(f"We have {cls.__population} robots.")


# 1.
droid = Robot("R2-D2", 2)
print(droid.age)  # 가능
print(droid.name)

# 2.
droid.age = 77  # 2번 없이는 불가능, property에 대해 이런 명령을 받으면 setter를 찾음
print(droid.age)

droid.age += 1
print(droid.age)

droid.age = -999
print(droid.age)
