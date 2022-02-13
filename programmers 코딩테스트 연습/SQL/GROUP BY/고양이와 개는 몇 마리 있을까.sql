-- 코드를 입력하세요
SELECT ANIMAL_TYPE, count(*) as count from ANIMAL_INS group by ANIMAL_TYPE order by ANIMAL_TYPE

-- select 순서: select ~ from ~where ~ group by~ having~ order by