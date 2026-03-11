import pandas as pd
import numpy as np
import random

data = [[1000,4.5],[2000,3.9],[2500,4.2]]
idx = ['kfc','mcdonald','schoolfood']
col=['price','rating']
df = pd.DataFrame(data=data,index=idx,columns=col).reset_index(names='food')
print(df)
print("====")
data = {
    'kfd':[2000,5],
    'abc':[144,4],
    'affds':[124,555]
}
col=['food','price','rating']
idx=[0,1,2]
df = pd.DataFrame(data=data,columns=col,index=idx)
print(df)