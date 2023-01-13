import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv("Virat_Kohli.csv")
print(df.head())

#total no of runs kohali has scroed
print("Total runs:",df["Runs"].sum())

#Fond out the total no balls he has faced
print("Total number of balls",df["BF"].sum())


#Find out the average strike of kohli

print("Average stricke of kohli => ",df["SR"].mean())


#Number of matchs he has played at different positions
print(df["Pos"].head(10))
position= df["Pos"].unique()
print(position)


df["Pos"]=df["Pos"].map({
    3.0: "Batting at 3",
    4.0: " Batting at 4",
    2.0: "Batting at 2",
    1.0: " Batting at 1",
    7.0: "Batting at 7",
    5.0: " Batting at 5",
    6.0: "Batting at 6"
})
pos_count =df["Pos"].value_counts()
print(pos_count)
print(type(pos_count))
# print(df[["Runs","Pos"]])

#Total runs scored in different prosition
pos_counts_value=pos_count.values
pos_counts_labels=pos_count.index

fig=plt.figure(figsize=(10,7))
plt.pie(pos_counts_value,labels=pos_counts_labels)
plt.show()

#Total sixes scored in different position
def show_pie_plots(df,key):
   counts= df[key].value_counts()
   print(counts)
   count_values=counts.values
   count_labels= counts.index
   fig = plt.figure(figsize=(10,7))
   plt.pie(count_values,labels=count_labels)
   plt.show()
# show_pie_plots(df,"Opposition")   

#number of matchs he played with different opposition
show_pie_plots(df,"Opposition")
# number of match he has played  at ground           
show_pie_plots(df,"Ground")
#total runs scored with diffrenet conturies
runs_at_pos=df.groupby("Pos")["6s"].sum()
print(runs_at_pos,type(runs_at_pos))
runs_at_pos_values = runs_at_pos.values
runs_at_pos_labels = runs_at_pos.index

fig = plt.figure(figsize = (10,7))
plt.bar(
    runs_at_pos_labels,
    runs_at_pos_values,
    color="blue",
    width=0.3

)
plt.show()

#total runs scored with diffrenet conturies
runs_at_contries= df.groupby("Opposition")["Runs"].sum()
# print(runs_at_contries,type(runs_at_contries))
runs_at_contries_values = runs_at_contries.values
runs_at_contries_labels = runs_at_contries.index

fig = plt.figure(figsize = (10,7))
plt.bar(
    runs_at_contries_labels,
    runs_at_contries_values,
    color="red",
    width=0.3

)
plt.show()


#number of centuries scored by him in 1st  and 2nd inings
centuries=df.query("Runs >=100")
print(centuries)

innings = centuries["Inns"].value_counts()
print(innings)
plt.pie(innings.values,labels=innings.index)
plt.show()
# plt.bar(inning,tons,width=0.3)

#Calculate the dismissals of kohli

#againt which teams he was scored the most runs.





















