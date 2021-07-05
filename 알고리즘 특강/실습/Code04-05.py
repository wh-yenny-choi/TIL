# 단순 연결 리스트 생성

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

# 전역 변수 부
memory = []
head, current, pre = None, None, None
# dataArray = ['다현', '정연', '쯔위', '사나', '지효']  # 데이터셋(DB, 크롤링...)
import random
dataArray = [random.randint(1000, 9999) for _ in range(20)]

# 메인 코드 부
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
