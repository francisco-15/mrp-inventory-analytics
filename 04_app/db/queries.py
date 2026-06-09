import pandas as pd
from .connection import engine
from .analytics import compute_economic_impact_by_department

# A class materials
def get_a_class_meterials():
    query = "select * from v_economic_value_class_a"

    return pd.read_sql(query, engine)

def get_economic_impact_a_class():
    query = "select sum(ECONOMIC_VALUE_USD) as economic_value_class_a  from v_economic_value_class_a"

    df = pd.read_sql(query, engine)
    return df


# stock dead
def get_economic_impact_dead_stock():
    query = "select * from v_economic_impact_dead_stock"

    return pd.read_sql(query, engine)

#  unspecified material requests
def get_economic_impact_unspecified():
    query = "select * from v_economic_impact_unspecified"

    return pd.read_sql(query, engine)

def get_unassigned_materials():
    query = "select MATERIAL from v_unspecified_requests"
    return pd.read_sql(query, engine)

def unspecified_dept_outputs():
    query = "select count(MATERIAL) from v_unspecified_requests"
    
    return pd.read_sql(query, engine)

def plot_financial_supplier_summary():
    query = "select SUPPLIER, TOTAL_AMOUNT, ABC_CLASSIFICATION from financial_supplier_summary"
    return pd.read_sql(query, engine)


# comparative inventary
def get_comparative_inventory():
    return pd.read_sql("select * from abc_representation", engine)

# economic impact by department
def get_economic_impact_by_department():
    df = pd.read_sql("select * from economic_impact_by_departments", engine)
    
    df.columns = df.columns.str.replace(r'[^A-Za-z0-9_]', '', regex=True)
    
    return df