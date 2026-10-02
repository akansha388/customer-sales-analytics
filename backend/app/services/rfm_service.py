import pandas as pd
from datetime import datetime

def calculate_rfm_segments(df_orders: pd.DataFrame, ref_date: datetime = None):
    if df_orders.empty:
        return pd.DataFrame()
        
    if ref_date is None:
        ref_date = pd.to_datetime(df_orders['order_date']).max()
        
    df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])
    
    rfm = df_orders.groupby('customer_id').agg({
        'order_date': lambda x: (ref_date - x.max()).days,
        'id': 'nunique',
        'total_amount': 'sum'
    }).reset_index()
    
    rfm.columns = ['customer_id', 'recency', 'frequency', 'monetary']
    
    rfm['r_score'] = pd.qcut(rfm['recency'].rank(method='first', ascending=False), q=5, labels=[1, 2, 3, 4, 5]).astype(int)
    rfm['f_score'] = pd.qcut(rfm['frequency'].rank(method='first'), q=5, labels=[1, 2, 3, 4, 5]).astype(int)
    rfm['m_score'] = pd.qcut(rfm['monetary'].rank(method='first'), q=5, labels=[1, 2, 3, 4, 5]).astype(int)
    
    def assign_segment(row):
        r, f, m = row['r_score'], row['f_score'], row['m_score']
        if r >= 4 and f >= 4 and m >= 4:
            return 'Champions'
        elif r >= 3 and f >= 3 and m >= 3:
            return 'Loyal Customers'
        elif r >= 4 and f <= 2:
            return 'Recent Customers'
        elif r <= 2 and f >= 3:
            return 'At Risk'
        elif r <= 2 and f <= 2:
            return 'Hibernating'
        else:
            return 'Promising Customers'
            
    rfm['segment'] = rfm.apply(assign_segment, axis=1)
    return rfm
