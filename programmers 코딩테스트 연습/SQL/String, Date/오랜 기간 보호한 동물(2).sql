-- 코드를 입력하세요
SELECT I.ANIMAL_ID, I.NAME 
from ANIMAL_INS I, ANIMAL_OUTS O
where I.ANIMAL_ID = O.ANIMAL_ID
order by O.DATETIME-I.DATETIME DESC limit 2

'''
datetime type은 뺄셈이 가능
'''