katok = ['가', '나', '다', '라', '마']

def delete_data(position):  # position만 파라메타 받음
    klen = len(katok)
    katok[position] = None

    for i in range(position + 1, klen, 1):
        katok[i -1] = katok[i]
        katok[i] = None

    del(katok[klen - 1])

delete_data(1)
print(katok)
delete_data(3)
print(katok)
