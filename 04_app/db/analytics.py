import pandas as pd
from .connection import engine

def load_clean_entries():
    return pd.read_sql("SELECT * FROM entries", engine) 

def load_clean_outputs():
    return pd.read_sql("SELECT * FROM outputs", engine)  

def melt_abc_summary(abc_summary_df):
    melted_df = abc_summary_df[['ABC_CLASSIFICATION', '%_MATERIAL', '%_TOTAL_VALUATION']].copy()
    melted_df.columns = ['ABC_CLASSIFICATION', 'INVENTORY SHARE (%)', 'ECONOMIC VALUE (%)']
    melted_plot = melted_df.melt(id_vars='ABC_CLASSIFICATION', var_name='METRIC', value_name='PERCENTAGE')
    return melted_plot

def compute_abc_analysis():
    entries = load_clean_entries()
    outputs = load_clean_outputs()
    
    master_price = entries.groupby('MATERIAL')['UNIT_PRICE_USD'].median().reset_index()
    outbound = outputs[['MATERIAL', 'QUANTITY']].copy()
    valuation = pd.merge(outbound, master_price, on='MATERIAL', how='left')
    
    abc_table = valuation.groupby('MATERIAL').agg(
        MOVEMENT_VOLUME=('QUANTITY', 'sum'),
        MEDIAN_UNIT_PRICE=('UNIT_PRICE_USD', 'first')
    ).reset_index()
    
    abc_table['MEDIAN_UNIT_PRICE'] = abc_table['MEDIAN_UNIT_PRICE'].fillna(0)
    abc_table['TOTAL_VALUATION'] = abc_table['MOVEMENT_VOLUME'] * abc_table['MEDIAN_UNIT_PRICE']
    abc_table = abc_table.sort_values('TOTAL_VALUATION', ascending=False).reset_index(drop=True)
    
    total_val = abc_table['TOTAL_VALUATION'].sum()
    abc_table['SHARE_PERCENTAGE'] = (abc_table['TOTAL_VALUATION'] / total_val) * 100
    abc_table['CUMULATIVE_PERCENTAGE'] = abc_table['SHARE_PERCENTAGE'].cumsum()
    abc_table = abc_table.round(2)
    
    def abc_classification(p):
        return 'A' if p <= 80 else ('B' if p <= 95 else 'C')
    
    abc_table['ABC_CLASSIFICATION'] = abc_table['CUMULATIVE_PERCENTAGE'].apply(abc_classification)
    
    abc_summary = abc_table.groupby('ABC_CLASSIFICATION').agg(
        MATERIAL=('MATERIAL', 'count'),
        TOTAL_VALUATION=('TOTAL_VALUATION', 'sum')
    ).reset_index()
    
    total_mats = abc_summary['MATERIAL'].sum()
    total_val_sum = abc_summary['TOTAL_VALUATION'].sum()
    abc_summary['%_MATERIAL'] = (abc_summary['MATERIAL'] / total_mats) * 100
    abc_summary['%_TOTAL_VALUATION'] = (abc_summary['TOTAL_VALUATION'] / total_val_sum) * 100
    abc_summary = abc_summary.round(2)
    
    melted_plot = melt_abc_summary(abc_summary)
    
    return abc_summary, melted_plot, abc_table

def save_abc_results_to_mysql():
    abc_summary, melted_plot, abc_table = compute_abc_analysis()
    abc_summary.to_sql('abc_summary', con=engine, if_exists='replace', index=False)
    melted_plot.to_sql('abc_representation', con=engine, if_exists='replace', index=False)
    abc_table.to_sql('abc_table_detail', con=engine, if_exists='replace', index=False)

def compute_economic_impact_by_department():
    _, _, abc_table = compute_abc_analysis()
    outputs = load_clean_outputs()
    
    economic = outputs.merge(
        abc_table[['MATERIAL', 'MEDIAN_UNIT_PRICE', 'ABC_CLASSIFICATION']],
        on='MATERIAL',
        how='left'
    )
    
    economic['ABC_CLASSIFICATION'] = economic['ABC_CLASSIFICATION'].replace({'B': '(B & C)', 'C': '(B & C)'})
    
    economic['ECONOMIC_IMPACT'] = economic['QUANTITY'] * economic['MEDIAN_UNIT_PRICE']
    
    summary = economic.groupby(['REQUESTING_DEPARTMENT', 'ABC_CLASSIFICATION'], as_index=False)['ECONOMIC_IMPACT'].sum()
    
    summary['ABC_CLASSIFICATION'] = pd.Categorical(summary['ABC_CLASSIFICATION'], categories=['A', '(B & C)'], ordered=True)
    
    return summary