# 데이터가 5개인 단순 연결 리스트 생성
class Node():  # 클래스라는 문법을 사용하여 Node 데이터형 정의
    def __init__(self):  # 데이터형을 생성할 때 자동으로 실행되는 부분
        self.data = None  # 데이터 저장 부분
        self.link = None  # 링크 저장 부분

# 첫 번째 노드를 생성하기 위한 코드
node1 = Node()
node1.data = '다현'

# 두 번째 노드를 생성하고, 첫 번째 노드의 링크로 연결하는 코드
node2 = Node()
node2.data = '정연'
node1.link = node2  # 첫 번째 노드의 링크에 두 번째 노드를 넣어 연결

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

# # 노드 삽입
# newNode = Node()
# newNode.data = '원희'
# newNode.link = node2.link
# node2.link = newNode

# print(node1.data, end=' ')
# print(node1.link.data, end=' ')
# print(node1.link.link.data, end=' ')
# print(node1.link.link.link.data, end=' ')
# print(node1.link.link.link.link.data, end=' ')

# 노드 삭제 : 중간 데이터 삭제
node2.link = node3.link
del(node3)

# 데이터가 5개인 다순 연결 리스트를 모두 출력 (line34~38 개선 버전)
current = node1
print(current.data, end=' ')
while current.link != None:
    current = current.link
    print(current.data, end=' ')


