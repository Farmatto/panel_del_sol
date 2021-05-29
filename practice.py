import pandas as pd
import os

file_list = os.listdir('INPUT')
os.chdir('INPUT')
one_file = str(file_list[0])

soda = pd.read_excel(one_file)
print(soda.head())
