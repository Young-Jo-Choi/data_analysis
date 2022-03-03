from typing import Union, List, Tuple, Optional, Dict
from typing_extensions import TypedDict

# type alias
value: Union[
    int, bool, Union[List[str], List[str], Tuple[int, ...]], Optional[Dict[str, float]]
] = 17

# 가독성과 재사용성이 너무 떨어진다.
def cal(
    v: Union[
        int,
        bool,
        Union[List[str], List[str], Tuple[int, ...]],
        Optional[Dict[str, float]],
    ]
) -> Union[
    int, bool, Union[List[str], List[str], Tuple[int, ...]], Optional[Dict[str, float]]
]:
    return v


# 위와 똑같은 코드를 다음과 같이 간소화시킬 수 있다.
# 주의) :대신 =을 입력하시오.
type_Value = Union[
    int, bool, Union[List[str], List[str], Tuple[int, ...]], Optional[Dict[str, float]]
]
value2: type_Value = 17


def cal2(v: type_Value) -> type_Value:
    return v


# Dict alias
ddd: Dict[str, Union[str, int]] = {"hello": "world", "world": "wow!!", "hee": 17}

# 다음과 같은 class를 만들어 Dictonary에 대한 alias 적용 가능
# 없는 key값을 추가해도 문제가 발생할 수 있음
class Point(TypedDict):
    x: int
    y: float
    # key z에 대해서는 string만 가능
    z: str
    w: int


point: Point = {"x": 8, "y": 8.4, "z": "12", "w": 12}
