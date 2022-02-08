## 개선된 선택 정렬

# 클래스와 함수 선언 부분
def selectionSort(ary):
    n = len(ary)  # 4개
    for i in range(0, n - 1):  # 사이클 (큰 반복 3회)
        minIdx = i
        for k in range(i + 1, n):  # 작은 반복
            if (ary[minIdx] > ary[k]):
                minIdx = k
        ary[i], ary[minIdx] = ary[minIdx], ary[i]
    return ary


# 전역변수 부분
import random
dataAry = [random.randint(50, 190) for _ in range(8)]

# 메인 코드 부분
print('정렬 전 :', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후 :', dataAry)


'''
<실습>
def selectionSort(ary):
    n = len(ary)
    for i in range(0, n - 1):
        minInx = 0
        for k in range(i + 1, n):
            if (ary[minInx] > ary[k]):
                minInx = k
        ary[i], ary[minInx] = ary[minInx], ary[i]
    return ary

import random
dataAry = [random.randint(50, 190) for _ in range(8)]
print('정렬전', dataAry)
dataAry = selectionSort(dataAry)
print('정렬후', dataAry)
'''