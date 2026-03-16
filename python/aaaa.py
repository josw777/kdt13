import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family']='Malgun Gothic'    # 글꼴 설정
plt.rcParams['axes.unicode_minus']=False

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

df.drop()
df.merge()
df.groupby('테마').count()
df.groupby('테마').agg()

df.corr(method='pearson',numeric_only=True)
df1.pivot('도시','연도','인구')
df.plot.pie(autopct=)
data = pd.read_csv('시군구별_9개도___산업별__규모별__사업체수_및_종사자수_성별__20260316112354.csv',skip)

result = pd.concat([df1, df2], ignore_index=True)
plt.pie()
plt.axis()