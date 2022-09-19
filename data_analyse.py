import pandas as pd

def data_analyse(exporeted_file):
    df = pd.read_csv(exporeted_file)
    df.sort_values(by= "Expires", inplace= True)
    df = df[df["Expires"].str.match("09/20/2022") == True]
    res = df[["Name", "Source", "TF", "CF", "Age", "Price", "Expires"]]
    res.to_csv("Spamzilla-Automation-Tool\output.csv")

# paste the path of exported file here
data_analyse("D:\Downloads\export-61508_2022-09-17-02-46-26.csv")