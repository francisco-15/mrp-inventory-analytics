import pandas as pd
from .connection import engine
from .analytics import compute_abc_analysis, compute_economic_impact_by_department

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

def unspecified_dept_outputs():
    query = "select count(MATERIAL) from v_unspecified_requests"
    
    return pd.read_sql(query, engine)

# comparative inventary
def get_comparative_inventory():
    return pd.read_sql("select * from abc_representation", engine)

# economic impact by department
def get_economic_impact_by_department():
    return compute_economic_impact_by_department()