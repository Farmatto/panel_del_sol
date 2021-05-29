import pandas as pd

# create dataframe
df_marks = pd.DataFrame({'name': ['Somu', 'Kiku', 'Amol', 'Lini'],
     'physics': [68, 74, 77, 78],
     'chemistry': [84, 56, 73, 69],
     'algebra': [78, 88, 82, 87]})

# create excel writer object
writer = pd.ExcelWriter('output.xlsx')
# write dataframe to excel
df_marks.to_excel(writer)
# save the excel
writer.save()
print('DataFrame is written successfully to Excel File.')
