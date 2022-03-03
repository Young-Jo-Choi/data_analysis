"""
Callable Types
"""


def add(a: int, b: int) -> int:
    return a + b


print(add(1, 3))

from typing import Callable

# 첫번째 인자값은 함수의 input, 두번째 인자값은 함수의 output
def foo(func: Callable[[int, int], int]) -> int:
    return func(2, 3)


print(foo(add))
