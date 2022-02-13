-- 코드를 입력하세요
SELECT * from PLACES where HOST_ID IN (
    SELECT HOST_ID from PLACES
    group by HOST_ID having count(HOST_ID) >= 2)
order by ID