import pandas as pd

df=pd.read_csv("Virat_Kohli.csv")
print(df.head(10))  #see first 10 data in give file
 
print(df.tail(10))     #see last 10 data in give file

# df.info()    

# print(df.shape)

print(df.describe())
# print(df["SR"].describe())  #single elements to find
print(df["Opposition"].describe()) 


run_frequency=df["Runs"].value_counts()
print(run_frequency)


new_df=df[["Runs","SR","Opposition"]]
print(new_df)

vs_aussies=df[df["Opposition"]=="v Australia"]
print(vs_aussies)


# Find all the match where virat score a century
tons=df[df["Runs"]>=100]
print(tons)
#Find all the matchs where Virat's stricke rate
#was>100
ton_sr=df[df["SR"]>100]
print(ton_sr)
#find all the matches where virat played with
#Srilanka and scored a Century
sril_cent=df[
    (df["Opposition"]=="v Sri Lanka") & (df["Runs"])
]
print(sril_cent)





def find_centuries(x):
    if x>=100:
        return "OG"
    else:
        return "NOOB"

df["Centuries"] =  df["Runs"].apply(find_centuries)
print(df.tail(10 ))          










