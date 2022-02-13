-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') as 날짜 from ANIMAL_INS
order by ANIMAL_ID
'''
DATE_FORMAT(DATE, 형식)을 통해 DATE의 형식을 바꿀 수 있습니다.
형식에는 %Y(4자리 연도), %y(2자리 연도), %m(월), %d(일), %H(24시간), %h(12시간), %i, %s가 있습니다.

++++ 2015라면 %y = 15, %Y = 2015
'''