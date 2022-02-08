# 단순 연결 리스트와 노드 삭제 함수

# 클래스 또는 함수 선언부
class Node():  # 클래스라는 문법을 사용하여 Node 데이터형 정의
    def __init__(self):  # 데이터형을 생성할 때 자동으로 실행되는 부분
        self.data = None  # 데이터 저장 부분
        self.link = None  # 링크 저장 부분

def printNodes(start):
    current = start
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def deleteNodes(deleteData):
    global memory, head, current, pre

    if head.data == deleteData:  # 첫 번째 노드 삭제
        current = head
        head = head.link
        del(current)
        return

    current = head  # 첫 번째 외 노드 삭제
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

# 전역 변수 선언 부분
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']  # 데이터셋(DB, 크롤링...)

# 메인 코드 부분
if __name__ == "__main__":  # C, Java, C++, C# ==> main()함수, 헤드가 길어질때

    node = Node
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

    deleteNodes("다현")
    printNodes(head)

    deleteNodes("쯔위")
    printNodes(head)

    deleteNodes("지효")
    printNodes(head)

    deleteNodes("원희")
    printNodes(head)