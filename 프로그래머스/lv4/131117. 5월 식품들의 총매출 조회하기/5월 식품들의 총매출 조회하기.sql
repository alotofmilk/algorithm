SELECT FOOD_PRODUCT.PRODUCT_ID, FOOD_PRODUCT.PRODUCT_NAME, SUM(FOOD_PRODUCT.PRICE * FOOD_ORDER.AMOUNT) AS TOTAL_SALES
FROM FOOD_PRODUCT
INNER JOIN FOOD_ORDER
    ON FOOD_PRODUCT.PRODUCT_ID = FOOD_ORDER.PRODUCT_ID
WHERE FOOD_ORDER.PRODUCE_DATE LIKE "2022-05%"
GROUP BY FOOD_PRODUCT.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, FOOD_PRODUCT.PRODUCT_ID ASC;