import pandas as pd
import numpy as np
arr= np.array([1,2,3,4,5])
print(arr)

data= {
    "name":[ "kunal","dolly","shree","krishna" ],
    "marks":[96,98,100,94],
    "cities":["nagpur","gondia","pune","mumbai"]
}
df=pd.DataFrame(data)
print(df)
print("Average:", df["marks"].mean())
print("Max:", df["marks"].max())
print("Min:", df["marks"].min())
topper=df[df["marks"] == df["marks"].max()]
print("topper \n" ,topper)
top2 = df.sort_values(by="marks", ascending=False).head(2)
print(top2)
top_pune = df[(df["marks"] > 90) & (df["cities"] == "pune")]
print(top_pune)