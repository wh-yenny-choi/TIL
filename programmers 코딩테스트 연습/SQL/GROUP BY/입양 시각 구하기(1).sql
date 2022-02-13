-- 코드를 입력하세요
SELECT hour(DATETIME) as HOUR, count(DATETIME) as COUNT from ANIMAL_OUTS
where hour(DATETIME) between 9 and 19
group by hour(DATETIME)
order by hour(DATETIME)

-- hour() 가 작동하는군...