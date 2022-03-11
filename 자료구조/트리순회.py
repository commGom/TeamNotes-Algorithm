
from tkinter import E


class Node:
    # 생성자 self.data left_node, right_node의 멤버변수 값에 값을 받는다
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


# 입력 예시
# 7
# A B C
# B D E
# C F G
# D None None
# E None None
# F None None
# G None None

# 받을 값 갯수 입력받기
n = int(input())
tree = {}

for i in range(n):
    # 입력 받을 때 루트노드, 왼쪽 자식 노드 오른쪽 자식 노드 입력받고
    data, left_node, right_node = input().split()
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
    # 해당 노드에 대하여 클래스로 정의한 왼쪽자식, 오른쪽 자식 정보 tree 딕셔너리 구조에 저장 만들어서
    tree[data] = Node(data, left_node, right_node)

# 전위 순회 (루트->왼->오)


def pre_order(node):
    # 루트 먼저
    print(node.data, end=" ")
    # 왼쪽 자식 노드
    if node.left_node != None:
        pre_order(tree[node.left_node])
    # 오른쪽 자식 노드
    if node.right_node != None:
        pre_order(tree[node.right_node])

# 중위 순회 (왼->루트->오)


def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end=' ')
    if node.right_node != None:
        in_order(tree[node.right_node])

# 후위 순회 (오->왼->루트)


def post_order(node):
    if node.right_node != None:
        post_order(tree[node.right_node])
    if node.left_node != None:
        post_order(tree[node.left_node])
    print(node.data, end=" ")


# 결과 확인
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])

# A B D E C F G
# D B E A F C G
# G F C E D B A
