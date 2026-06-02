# creating database
create schema if not exists mrp_movements;

# selecting schema
use mrp_movements;

# creating entries table
create table if not exists entries (
`SAP_CODE` varchar(50),
`DATE` datetime,
`MATERIAL` varchar(300),
`UNIT_OF_MEASURE` varchar(50),
`QUANTITY` int,
`DELIVERY_NOTE_N°` varchar(200),
`SUPPLIER` varchar(200),
`UNIT_PRICE_USD` decimal(12,2)
);

# creating outputs table
create table if not exists outputs (
`SAP_CODE` varchar(50),
`DATE` datetime,
`MATERIAL` varchar(300),
`UNIT_OF_MEASURE` varchar(50),
`QUANTITY` int,
`REQUESTING_DEPARTMENT` varchar(70),
`REQUESTED_BY` varchar(70),
`APPROVED_BY` varchar(70)
);