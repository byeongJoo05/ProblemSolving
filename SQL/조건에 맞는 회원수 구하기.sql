--date의 관련된 문법
--DATE_FORMAT(날짜, 'FORMAT') - 날짜를 해당 포맷으로 변환
--DATE(날짜) - 날짜를 '연도-월-일'로 변환
--YEAR(날짜) - 날짜의 연도 반환
--MONTH(날짜) - 날짜의 월 반환

SELECT count(*) as USERS
from user_info
where (age between 20 and 29) and year(joined) = '2021'