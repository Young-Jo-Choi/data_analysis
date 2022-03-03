"""
Class Type
"""


class Hello:
    def world(self) -> int:
        return 7


class World:
    pass


# class에 대한 instance를 타이핑할 때 클래스명을 써주면 된다.
hello: Hello = Hello()
# hello: "Hello" = Hello() 역시 가능
world: World = World()


def foo(ins: Hello) -> int:
    return ins.world()  # 힌트를 주면 .찍었을때 자동완성 가능


print(foo(hello))

"""
print(foo(world))를 mypy로 실행하면 
error: Argument 1 to "foo" has incompatible type "World"; expected "Hello" 가 출력됨
"""


class Node:
    # node로 자기 자신을 받음
    # class안에서 자기 자신을 typing할 때는 "Node" 와 같이 하면 가능, 그냥 Node는 에러
    from typing import Optional

    def __init__(self, data: int, node: Optional["Node"] = None):
        self.data = data
        self.node = node


# node2 = Node(12, None)
node2 = Node(12)
node1 = Node(27, node2)
node0 = Node(30, node1)

"""
Union Type
"""

# 처음에는 정수형을 대입했다가 로직에 따라 문자열도 대입을 하고 싶다면?
from typing import Union

xxx: Union[int, str] = 3
xxx = "17"


def foo2(x: Union[int, str]) -> Union[int, str]:
    return x


print(foo2(xxx))

"""
Optional Type : 있을 수도 있고, 없을 수도 있는 객체
"""

xxx2: Union[str, None] = "amamov"
xxx2 = None

# 조금 더 간소화
from typing import Optional

xxx3: Optional[str] = "amamov"
xxx3 = None


def foo3(name: str) -> Optional[str]:
    if name == "amamov":
        return None
    else:
        return name


xxx4: Optional[str] = foo3("amamov")

"""
Final Type
"""

from typing_extensions import Final

# final로 상수가 되면 변경 불가(기본적으로 python에서는 제공하지 않는 변수형임)
RATE: Final = 300

"""RATE = 400  # In mypy : error: Cannot assign to final name "RATE"
print(RATE)"""
