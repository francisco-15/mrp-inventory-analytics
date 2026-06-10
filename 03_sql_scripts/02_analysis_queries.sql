# Selecting database
use mrp_movements;

# economic value in class A material
create or replace view v_economic_value_class_a as 
SELECT 
    outputs.SAP_CODE,
    outputs.MATERIAL,
    round(outputs.TOTAL_OUTPUTS * prices.MEDIAN_PRICE, 2) AS ECONOMIC_VALUE_USD,
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
create or replace VIEW v_economic_impact_dead_stock AS 
SELECT SUM(TOTAL_AMOUNT) AS TOTAL_DEAD_STOCK_VALUE_USD 
FROM financial_supplier_summary 
WHERE ABC_CLASSIFICATION = 'DEAD STOCK'
;

# Unspecified material requests
create or replace view  v_unspecified_requests as
select
	SAP_CODE, `DATE`, MATERIAL, UNIT_OF_MEASURE, QUANTITY, REQUESTING_DEPARTMENT, `REQUESTED_BY`, `APPROVED_BY`
from outputs
where	
	REQUESTING_DEPARTMENT = 'UNSPECIFIED'
;

# Economic Impact of Materials with Unattributed Cost Centers
create or replace view v_material_unit_costs AS
SELECT 
    SAP_CODE, 
    AVG(UNIT_PRICE_USD) as avg_unit_cost
FROM entries
GROUP BY SAP_CODE
;

create or replace view v_unspecified_impact_details AS
SELECT 
    u.SAP_CODE,
    u.MATERIAL,
    (u.QUANTITY * c.avg_unit_cost) AS TOTAL_IMPACT
FROM v_unspecified_requests u
LEFT JOIN v_material_unit_costs c ON u.SAP_CODE = c.SAP_CODE
;

create or replace view v_economic_impact_unspecified AS
SELECT 
    round(sum(u.QUANTITY * c.avg_unit_cost), 2) AS TOTAL_IMPACT
FROM v_unspecified_requests u
LEFT JOIN v_material_unit_costs c ON u.SAP_CODE = c.SAP_CODE
;

    