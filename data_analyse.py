import pandas as pd
from datetime import datetime, timedelta
import os

# Rename exported file
# for (root, dirs, files) in os.walk('D:\ASM\SpamzillaExport\Spamzilla-Automation-Tool\data', topdown=True):
#     print (files)
# os.rename(f"D:\ASM\SpamzillaExport\Spamzilla-Automation-Tool\data/{files[0]}", "D:\ASM\SpamzillaExport\Spamzilla-Automation-Tool\data\exported_data.csv")

def data_analyse(exporeted_file):
    for (root, dirs, files) in os.walk('D:\ASM\SpamzillaExport\Spamzilla-Automation-Tool\data', topdown=True):
        print (files)
    os.rename(f"D:\ASM\SpamzillaExport\Spamzilla-Automation-Tool\data/{files[0]}", "D:\ASM\SpamzillaExport\Spamzilla-Automation-Tool\data\exported_data.csv")
    tomorrow = datetime.now() + timedelta(days = 1)
    dt_string = tomorrow.strftime("%m/%d/%Y") 
    print(dt_string)
    df = pd.read_csv(exporeted_file)
    df.sort_values(by= "Expires", inplace= True)
    df = df[df["Expires"].str.match(dt_string) == True]
    res = df[["Name", "Source", "TF", "CF", "Age", "Price", "Expires"]]
    res.to_csv("Spamzilla-Automation-Tool\output.csv")

# paste the path of exported file here
# data_analyse("Spamzilla-Automation-Tool\data\exported_data.csv")
