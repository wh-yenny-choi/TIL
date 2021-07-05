# 단순 연결 리스트와 노드 삽입 함수

# 클라스 함수 선언 부분
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()
    
def insertNodes(findData, insertData):
    global memory, head, current, pre
    
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    
    current = head
    while current.link != None:  # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    node = Node()  # 마지막 노드 삽입
    node.data = insertData
    current.link = node

# 전역변수 부분
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

# 메인 코드 부분
if __name__ == "__main__":

    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1: ]: # ['정연', '쯔위', '사나', '지효']
        pre = node
        node = Node()  # 정연, 쯔위 ...
        node.data = data  # 정연, 쯔위...
        pre.link = node
        memory.append(node)

        printNodes(head)

    insertNodes('다현', '화사')
    printNodes(head)

    insertNodes('사나', '솔라')
    printNodes(head)

    insertNodes('원희', '문별')
    printNodes(head)
