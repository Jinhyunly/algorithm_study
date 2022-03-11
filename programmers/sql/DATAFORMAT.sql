-- 코드를 입력하세요 
-- DATE_FORMAT(DATE, 형식)을 통해 DATE의 형식을 바꿀 수 있습니다. 
-- 형식에는 %Y(4자리 연도), %y(2자리 연도), %m(월), %d(일), %H(24시간), %h(12시간), %i, %s가 있습니다.

SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS "날짜" 
    FROM ANIMAL_INS