-- 코드를 입력하세요
SELECT NAME, count(*) as COUNT from ANIMAL_INS
where NAME IS NOT NULL
group by NAME having count(NAME) >= 2
order by NAME