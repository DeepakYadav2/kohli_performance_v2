import pandas as pd


data = {
    "apples": [4,3,6,1],
    "orange": [3,7,4,1]
}

index_title=[
    "Aaron","shaun","James","Wilson"
]
df=pd.DataFrame(data,index=index_title)
print(df)
# print(df.loc["Aaron"]["apples"])  #to find the single elements it is row indexing
print(df["orange"].iloc[1:])      #it is column indexing
# print(df["orange"].iloc[0:])

print(type(df))














