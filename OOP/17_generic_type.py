"""
데이터 형식에 의존하지 않고, 하나의 값이 여러 다른 데이터 타입들을 가질 수 있는 기술
"""

from typing import Generator, Generic, Optional, Union, TypeVar

ARM = TypeVar("ARM", int, float, str)  # Generic 변수, int,float, str 세 개 가능
HEAD = TypeVar("HEAD")


class Robot(Generic[ARM]):
    def __init__(self, arm: ARM, head: int):
        # 암호
        self.arm = arm
        self.head = head

    def decode(self):
        # 암호해독하는 코드, 복잡
        # self.arm이 str일 수도, int일 수도 있으나 self.arm과 같은 타입의 변수를 선언하고자 할 때
        # 처음 arm을 int로 선언한다면 ARM은 모두 int가 된다.(다른 타입도 마찬가지)
        bbb: Optional[ARM] = None
        pass


robot1 = Robot[int](122314, 23908409)  # [int]는 [ARM]이 어떤 타입으로 역할할지 지정
robot2 = Robot[str]("123123", 235325)
robot3 = Robot[float](123.1411, 63463)

# 확장
class Robot2(Generic[ARM, HEAD]):
    def __init__(self, arm: ARM, head: HEAD):
        self.arm = arm
        self.head = head

    def decode(self):
        bbb: Optional[ARM] = None
        pass


robot2_1 = Robot2[int, int](122314, 23908409)  # [int]는 [ARM]이 어떤 타입으로 역할할지 지정
robot2_2 = Robot2[str, int]("123123", 235325)
robot2_3 = Robot2[float, str](123.1411, "63463")

# 상속
class Siri(Generic[ARM, HEAD], Robot2[ARM, HEAD]):
    pass


siri1 = Siri[int, int](12312, 6345)

""" 
function
"""


def test(x: ARM) -> ARM:
    print(x)
    print(type(x))
    return x


test(898)
