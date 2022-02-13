-- 코드를 입력하세요
SELECT distinct CART_ID from CART_PRODUCTS
where NAME = 'Milk' and CART_ID in (
    select distinct CART_ID from CART_PRODUCTS  
    where NAME = 'Yogurt')
order by CART_ID