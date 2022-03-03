"""
객체 내에 있는 변수들은 __dict__를 통해서 관리가 된다.
__slots__을 통해 변수를 관리
파이썬 인터프리터에게 통보, 해당 클래스가 가지는 속성을 제한한다.
__dict__를 통해 관리되는 객체의 성능을 최적화한다. 
    -> 다수의 객체 생성시 메모리 사용 공간이 대폭 감소한다.
"""


class WithOutSlotClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


wos = WithOutSlotClass("amamov", 12)
print(wos.__dict__)  # {'name': 'amamov', 'age': 12}

wos.__dict__["hello"] = "world"
print(wos.__dict__)  # {'name': 'amamov', 'age': 12, 'hello': 'world'}
print(wos.hello)


print("Up : withOutSlot , \nDown : WithSlot")


class WithSlotClass:
    __slots__ = ["name", "age"]

    def __init__(self, name, age):
        self.name = name
        self.age = age


ws = WithSlotClass("amamov", 12)
print(ws.name)
print(ws.__slots__)
# print(ws.__dict__)  # 'WithSlotClass' object has no attribute '__dict__'
# dictionary 형태가 아닌 list 형태로 관리 + name과 age 속성만 사용할 수 있도록

"""
성능테스트 : 메모리 사용량 비교
"""
import timeit


def repeat(obj):
    def inner():
        obj.name = "amamov"
        obj.age = 222
        del obj.name
        del obj.age

    return inner


use_slot_time = timeit.repeat(repeat(ws), number=499999)
no_slot_time = timeit.repeat(repeat(wos), number=499999)

print("use slot : ", min(use_slot_time))
print("no slot : ", min(no_slot_time))
