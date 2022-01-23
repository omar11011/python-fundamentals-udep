import pandas as pd

def adjustDate(df):
    df['date'] = df['year'].astype('str') + '-' + (df['quarter'] * 3 - 2).astype('str').str.pad(2, fillchar = '0')
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m')
    df = df[ df.date < '2022-01-01' ]
    
    return df