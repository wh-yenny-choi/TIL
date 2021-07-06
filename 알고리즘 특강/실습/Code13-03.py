## 정렬된 데이터의 이진 검색

# 클래스와 함수 선역 부분
def binSearch(ary, fData):
    pos = -1  # 리턴할 값
    start = 0
    end = len(ary) - 1

    while (start <= end):
        mid = (start + end) // 2
        if fData == ary[mid]:
            return mid
        elif fData > ary[mid]:
            start = mid + 1
        else:  # fData < ary[mid]
            end = mid - 1
    return pos

# 전역 변수 부분
dataAry = [50, 60, 105, 120, 150, 160, 162, 168, 177, 188]
findData = 162

# 메인 코드 부분
print('배열 :', dataAry)
postion = binSearch(dataAry, findData)
if postion == -1:
    print(findData,'(이)가 없네요.')
else:
    print(findData, '(은)는', postion, '위치에 있음')
