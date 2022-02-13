-- 코드를 입력하세요
SELECT count(distinct NAME) as count from ANIMAL_INS where NAME is not NULL
-- 집계함수 쓸때 distinct는 ()안에 쓰기