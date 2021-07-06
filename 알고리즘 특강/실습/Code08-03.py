# 이진 탐색 트리의 삽입 작동

# 함수 선언 부분
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

# 전역 번수
memory = []
root = None
# 데이터베이스 또는 크롤링으로 얻은 로우 데이터 집합
nameAry = ['블랭핑크', '레드벨벳', '에이핑크', '걸스데이', '트와이스', '마마무']


# 메인 코드
node = TreeNode()
# 첫번째 노드 생성
name = nameAry[0]
node.data = name
memory.append(node)
root = node

for name in nameAry[1: ]:
    node = TreeNode()
    node.data = name
    current = root
    while True:
        if name < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right

    memory.append(node)

print(memory)
print('이진 탐색 트리 구성 완료')

## 이진 탐색 트리의 검색 작동

# 함수 선언 부분
findName = '마마무'
current = root

print(findName, '를 찾기')
while True:
    if current.data == findName:
        print(findName, '를 찾았음')
        break
    elif findName < current.data:
        if current.left == None:
            print('못 찾았음')
            break
        current = current.left
    else:
        if current.right == None:
            print('못 찾았음')
            break
        current = current.right







