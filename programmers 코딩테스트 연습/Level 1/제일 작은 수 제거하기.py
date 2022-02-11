def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        return arr
    else:
        return [-1]

# 좋아요 순
def rm_small(arr):
    return [i for i in arr if i > min(arr)]