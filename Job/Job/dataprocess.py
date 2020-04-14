import pandas as pd

merge_dt = pd.read_csv('data/chizhou/zhaopinurl.csv')
merge_dt = merge_dt.drop_duplicates()
merge_dt.to_csv("data/chizhou/zhaopinurl1.csv",encoding='utf-8')