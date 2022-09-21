from data_analyse import data_analyse
from automation import App

def Spamzilla_Tool():
    data_analyse()
    App("D:\ASM\SpamzillaExport\Spamzilla-Automation-Tool\data\exported_data.csv")

Spamzilla_Tool()