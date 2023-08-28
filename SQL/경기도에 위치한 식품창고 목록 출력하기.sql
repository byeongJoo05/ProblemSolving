-- 코드를 입력하세요
/*
IFNULL(NULL이 들어갈 속성, 바꿀 레코드값)

where 절에서 like 문법을 통해 특정 문자열을 추출 가능함
*/

SELECT warehouse_id, warehouse_name, address, IFNULL(freezer_yn,'N') as freezer_yn
from food_warehouse
where address like '%경기%'
order by warehouse_id