# Selecting database
use mrp_movements;

# economic value in class A material
SELECT 
    outputs.SAP_CODE,
    outputs.MATERIAL,
    (outputs.TOTAL_OUTPUTS * prices.MEDIAN_PRICE) AS ECONOMIC_VALUE_USD,
    RANK() OVER (ORDER BY (outputs.TOTAL_OUTPUTS * prices.MEDIAN_PRICE) DESC) AS MATERIAL_ECONOMIC_RANK
FROM (
    SELECT SAP_CODE, MATERIAL, SUM(QUANTITY) AS TOTAL_OUTPUTS
    FROM outputs
    GROUP BY SAP_CODE, MATERIAL
) AS outputs
INNER JOIN (
    SELECT 
        SAP_CODE,
        AVG(UNIT_PRICE_USD) AS MEDIAN_PRICE
    FROM (
        SELECT 
            SAP_CODE,
            UNIT_PRICE_USD,
            ROW_NUMBER() OVER (PARTITION BY SAP_CODE ORDER BY UNIT_PRICE_USD ASC) AS row_num,
            COUNT(*) OVER (PARTITION BY SAP_CODE) AS total_rows
        FROM entries
    ) AS sorted_entries
    WHERE row_num IN (FLOOR((total_rows + 1) / 2), CEIL((total_rows + 1) / 2))
    GROUP BY SAP_CODE
) AS prices ON outputs.SAP_CODE = prices.SAP_CODE
limit 19
;

# Dead stock valuation
select
	sum(entries.QUANTITY * entries.UNIT_PRICE_USD) AS TOTAL_DEAD_STOCK_VALUE_USD
FROM entries 
LEFT JOIN outputs ON entries.SAP_CODE = outputs.SAP_CODE
where outputs.SAP_CODE is null
;

# Unspecified material requests
select
	SAP_CODE, DATE, MATERIAL, UNIT_OF_MEASURE, QUANTITY, REQUESTING_DEPARTMENT, `REQUESTED BY`, `APPROVED BY`
from outputs
where	
	REQUESTING_DEPARTMENT = 'UNSPECIFIED'
;

    