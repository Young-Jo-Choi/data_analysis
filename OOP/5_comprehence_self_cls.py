"""
self의 이해
- self는 인스턴스 객체이다.
- 클래스 안에 있는 self의 주소와 만들어진 인스턴스의 주소는 같다. 즉 self는 인스턴스 그 자체
"""


class SelfTest:
    # 클래스 변수
    name = "amamov"

    def __init__(self, x):
        self.x = x

    @classmethod
    def func1(cls):
        print(f"cls : {cls}")
        print("func1")

    # 인스턴스 메서드
    def func2(self):
        print(f"self:{self}")
        print(f"class안의 self 주소 : {id(self)}")
        print("func2")


test_obj = SelfTest(17)
test_obj.func2()
SelfTest.func1()
print("인스턴스의 주소 : ", id(test_obj))

"""
self:<__main__.SelfTest object at 0x00000228AA3FE208>
class안의 self 주소 : 2373678260744
func2
cls : <class '__main__.SelfTest'>
func1
인스턴스의 주소 :  2373678260744

- class안의 self 주소와 인스턴스의 주소는 같다. (self는 인스턴스 그 자체)
- cls는 클래스 자체를 가리킨다.
"""


# 인스턴스를 통해 class method를 실행하고 class 변수를 찾더라도 class namespace에서 찾아 실행한다.
test_obj.func1()
print(test_obj.name)
