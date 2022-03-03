"""
1. Type Hint
2. mypy, pyright : runtime에서 type 체크
    mypy 실행 : 터미널에서 mypy Script.py 입력 -->
         힌트에 대한 에러 개수까지 위치와 함께 체크해준다. 문제없으면 성공 출력
         단 결과 출력은 없음, mypy Script.py && Script.py
    pyright 실행(설치위해서는 node.js 필요) : 
        동일하지만 가상환경에는 설치를 못했으니 cmd를 켜서 실행해보시오
    팁) 거대한 스크립트를 mypy나 pyright로 테스트하기보다는 함수,기능별로 쪼개서 test.py 파일을 만들어
        각각에 대해 mypy나 pyright로 검사하는 것이 좋음

"""

int_var: int = 88
# error_int_var: str = 88
str_var: str = "hello world"
float_var: float = 88.9
bool_var: bool = True

list_var_temp: list = [1, 2, 3]
print(list_var_temp)
# print(error_int_var)
# print(type(error_int_var))

from typing import List, Tuple, Dict, Any

list_var: List[int] = [1, 2, 3]
list_var2: List[str] = ["1", "2", "3"]
tuple_var: Tuple[int, ...] = (1, 3, 5)
dic_var: Dict[str, int] = {"hello": 47}

# 주로 이런 Hint는 여러 사람과의 협업을 원활히 하기 위해
# 에러 반환에 대한 강제성은 없음
def cal_add(x: int, y: int) -> int:
    return x + y


# Any는 아무것이나 넣어도 된다는 의미, Any는 명시적 힌트를 안하는 경우도 있음
def type_check(obj: Any, typer) -> None:
    if isinstance(obj, typer):
        pass
    else:
        raise TypeError(f"Type Error : {typer}")


# 검증하는 함수를 넣음으로써 정교한 타입체크
def call_add_val(x: int, y: int) -> int:
    type_check(x, int)
    type_check(y, int)
    return x + y


# print(cal_add("1", "2"))
# 타입을 체크하는 함수
print(isinstance(88, int))
print(isinstance("gg", bool))

print(call_add_val(1, 3))
# print(call_add_val("1", "3")) # 에러가 남
