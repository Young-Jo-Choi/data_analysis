"""
선입선출


[Node Class]
- item
- pointer :  다음 node를 가리키므로 다음 node를 저장하고 아무 것도 가리키지 않으면 None을 저장한다.

[Linked List]
- head : 가장 첫 번째 node, node가 없으면 None을 저장한다.
- length : int 타입, 현재 노드(데이터)의 개수를 의미한다.

[Stack] : Linked List를 상속받는다.
- enque : 넣기
- deque : 빼기
"""


class Node:
    def __init__(self, item, pointer=None):
        self.item = item
        self.pointer = pointer


class LinkedList:
    def __init__(self, head):
        self.head = None

    @property
    def length(self):
        cnt = 1
        cur_node = self.head
        if cur_node is None:
            return 0
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
            cnt += 1
        return cnt


class Queue(LinkedList):
    def enque(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.node
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
        cur_node.pointer = new_node

    def deque(self):
        if self.head is None:
            raise ValueError("The Queue is empty")
        if self.head.pointer is None:
            self.head = None
            return self.head.item
        self.head = self.head.pointer
        return self.head.item
