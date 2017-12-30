import pandas as pd

df = pd.read_excel("file:///E:\Chicago_E_Drive\Deepak%20DOCs\Study\Data%20Analytics\Sample_Data\ManUtdPlayers.xlsx")

op = df.iloc[[4,9,20,26]].sum()

print("Output: " + op)