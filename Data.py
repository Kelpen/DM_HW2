import pandas as pd
import numpy as np


# Columns
# Info
# ['No', '性別_Gender', '年齡_Age', '共病症_Comorbidities',
# '三個月內曾使用過抗生素_Used antibiotics within 3 months',
# '三個月內曾長過的細菌_Bacteria grown in 3 months', 'Target']

# TPR
# ['No', '執行時間_Time', 'T', 'P', 'R', 'NBPS', 'NBPD']

# This function returns datasheet contents in two 2-D numpy arrays
def read_xlsx(file_name):
    d = pd.read_excel(file_name, engine='openpyxl', sheet_name=['Info', 'TPR'])
    return d['Info'].to_numpy(), d['TPR'].to_numpy()

