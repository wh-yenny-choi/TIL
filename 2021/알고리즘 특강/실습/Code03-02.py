katok = ['가', '나', '다', '라', '마']

def insert_data(position, friend):
    katok.append(None)
    klen = len(katok)

    for i in range(klen - 1, position, -1):   # position => 지정위치
        katok[i] = katok[i - 1]
        katok[i - 1] = None

    katok[position] = friend

insert_data(2, '바')   # 2번째 위치 (지정위치)에 '바' 삽입
print(katok)
insert_data(6, '사')   # 6번째 위치 (지정위치)에 '사' 삽입
print(katok)