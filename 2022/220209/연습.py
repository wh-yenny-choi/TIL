# # 6-10 위에서 아래로
# n = int(input())
# array = []
# for i in range(n):
#     array.append(int(input()))
#
# print(sorted(array, reverse=True))

# # 6-11 성적이 낮은 순서대로 학생 출력
# n = int(input())
# array = []
#
# for i in range(n):
#     data = input().split()
#     array.append((data[0], int(data[1])))
#
# array = sorted(array, key = lambda x: x[1])
#
# for student in array:
#     print(student[0], end=' ')

# 6-12 두 배열의 원소 교체
n, k =map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))