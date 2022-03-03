"""
스택(stack)이란 쌓아 올린다는 것을 의미한다.
따라서 스택 자료구조라는 것은 책을 쌓는 것처럼 차곡차곡 쌓아 올린 형태의 자료구조를 말한다.

[Node Class]
- item
- pointer :  다음 node를 가리키므로 다음 node를 저장하고 아무 것도 가리키지 않으면 None을 저장한다.

[Linked List]
- head : 가장 첫 번째 node, node가 없으면 None을 저장한다.
- length : int 타입, 현재 노드(데이터)의 개수를 의미한다.

[Stack] : Linked List를 상속받는다.
- push(item) : Stack 자료구조에 item을 받아 노드를 만든 다음 밀어넣는다.
- pop() : Stack 자료구조에서 마지막 node를 제거하고 해당 Item을 반환한다.
"""
from typing import Union, Optional, Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, item: T, pointer: Optional["Node"] = None):
        self.item = item
        self.pointer = pointer


class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None

    @property
    def length(self) -> int:
        if self.head is None:
            return 0
        cur_node = self.head
        count: int = 1
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
            count += 1
        return count

    def __str__(self) -> str:
        result: str = ""
        if self.head is None:
            return result
        cur_node = self.head
        result += f"{cur_node.item}"
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
            result += f", {cur_node.item}"
        return result


class Stack(Generic[T], LinkedList[T]):
    def push(self, item: T) -> None:
        new_node: Node[T] = Node[T](item=item)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
        cur_node.pointer = new_node

    def pop(self) -> T:
        if self.head is None:
            raise ValueError("Stack is empty")
        else:
            cur_node = self.head
        if cur_node.pointer is None:
            self.head = None
            return cur_node.item
        while cur_node.pointer.pointer is not None:
            cur_node = cur_node.pointer
        result = cur_node.pointer
        cur_node.pointer = None
        return result.item


if __name__ == "__main__":
    stack = Stack()
    stack.push(12)
    stack.push(14)
    stack.push(16)
    stack.push(5)
    print(stack.pop())
    print(stack.head)
    print(stack.length)
    print(stack.head.item)

    print(stack)
