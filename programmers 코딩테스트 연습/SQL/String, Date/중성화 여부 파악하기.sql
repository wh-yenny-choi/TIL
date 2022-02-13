-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME,
IF((SEX_UPON_INTAKE like 'Neutered%') or (SEX_UPON_INTAKE like 'Spayed%'), 'O', 'X') as '중성화'
from ANIMAL_INS 
order by ANIMAL_ID

-- IF(조건문, TRUE, FALSE)