def solution(name):
    answer = 0
    # 왼쪽에서 오른쪽으로만 이동시 좌, 우 조작 횟수
    min_value = len(name)
    next_idx = 0

    for idx, alpha in enumerate(name):
        # 위, 아래 조작(알파벳) 횟수의 최솟값 구하기
        answer += min(ord(alpha) - ord('A'), ord('Z') - ord(alpha) + 1)
        # 좌, 우 조작(위치) 횟수의 최솟값 구하기
        next_idx = idx + 1

        # 범위 설정
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1  # 현재 위치 이후 연속된 A 다음의 문자를 가리킴
        # 1) 한 방향(왼 -> 오)으로만 이동하는 경우
        # 2) 오른쪽 -> 왼쪽 이동 경우 비교하여 최솟값 찾기

'''
첫번째는 문자열 길이와 조작 횟수가 같다.
두번째는 특정 문자까지 이동한 후(해당 문자의 인덱스) 다시 처음 글자로 되돌아가(+ 해당 문자의 인덱스) 연속된 A문자의 다음 문자까지 마지막 위치에서부터 거꾸로 이동(+ 문자열 길이 - 연속된 A문자가 끝나는 위치 + 1)하면 된다.
'''
        min_value = min(min_value, idx + idx + len(name) - next_idx)
    answer += min_value

    return answer

'''
enumerate() 함수는 기본적으로 인덱스와 원소로 이루어진 터플(tuple)을 만들어줍니다

ord(문자)
하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
ord('a')를 넣으면 정수 97을 반환합니다.
'''
