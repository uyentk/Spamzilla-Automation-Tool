from automation import App
from data_analyse import data_analyse

def Spamzilla_Tool():
    App()
    print("Start to data analysing")
    data_analyse("Spamzilla-Automation-Tool\data\exported_data.csv")

Spamzilla_Tool()