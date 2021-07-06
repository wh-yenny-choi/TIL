## 배열에서 최솟값 위치를 값는 함수

# 함수 선언
def findMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if (ary[minIdx] > ary[i]):
            minIdx = i
    return minIdx


'''
<실습>
# 전역 변수, 메인 코드
testAry = [55, 88, 33, 77]
minPos = findMinIndex(testAry)
print('최솟값 :', testAry[minPos])

def minIndex(ary):
    min = 0
    for i in range(1, len(ary)):
        if (ary[min] > ary[i]):
            min = i
    return min

minArry = [55, 88, 33, 77]
minP = minIndex(minArry)
print(minArry[minP])
'''