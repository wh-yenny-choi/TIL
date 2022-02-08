
def findMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if (ary[minIdx] > ary[i]):
            minIdx = i
    return minIdx

# 전역 변수
import random
before = [random.randint(50, 190) for _ in range(8)]
after = []

# 메인 코드
print('정렬 전 :', before)
for _ in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])
print('정렬 후:', after)


'''
<실습>
def findMinIndex(ary):
    minIdx = 0
    for i in range(len(ary)):
        if ary[minIdx] > ary[i]:
            minIdx = i
    return minIdx
    
import random
before = [random.randint(50, 190) for _ in range(8)]
after = []

print('정렬전', before)
for _ in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])

print('정렬후', after)

<퀴즈>한글 배열을 30글자 만들고, 내림차순으로 정렬하기
import random
KorAry = [random.randint(0, 99999) for _ in range(1, 31)]

sorted(KorAry)
print(KorAry)
'''

