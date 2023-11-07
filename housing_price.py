import pandas as pd
import numpy as np



df = pd.read_csv('/home/sandeep/disk_C/csv_file/all/test.csv')
df.nunique()
df = df.drop(['Id'] , axis= 1)
df = df.drop(df.nunique()=1 , axis= 1)