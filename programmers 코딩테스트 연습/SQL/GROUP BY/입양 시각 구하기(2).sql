SET @HOUR :=-1;
SELECT(@HOUR:=@HOUR+1) AS HOUR,
(SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME)=@HOUR) AS COUNT
FROM ANIMAL_OUTS
WHERE @HOUR<23

'''
SET @변수명 = '값';
SET @변수명 := '값'; 
위의 2가지 방법으로 MySQL에서 변수를 선언할 수 있습니다.
SET 명령어를 사용한 변수 선언 시 '=' 와 ':=' 2가지 방법은 차이가 없습니다.
하지만 SET을 제외한 다른 쿼리문(SELECT 등)은 '=' 를 비교연산자(comparison operator)로 인식하기 때문에, SET이 아닌 쿼리문에서는 반드시 대입 연산자(assignment operator) ':='을 사용해 야 합니다.
결론적으로 보면 '='와 ':=' 차이는 아래와 같습니다.
'=' : MySQL에서 대입연산자, 비교연산자 2가지로 사용 됨 (SET 명령어에서만 대입 연산자로 인식)
':=' : MySQL에서 대입 연산자로만 사용 됨 
변수 사용 시 명시적으로 대입 연산자의 의미만을 갖는 ':=' 의 사용을 권장합니다. 

출처: https://mentha2.tistory.com/98 [행궁동 데이터 엔지니어]
'''
