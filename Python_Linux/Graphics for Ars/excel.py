import pandas as pd
import xlrd
rb = xlrd.open_workbook('test.xlsx',formatting_info=False)
sheet = rb.sheet_by_index(0)
row = []
for i in range(sheet.nrows):
    r = sheet.row_values(i)
    row.append(r)
print (row)
df = pd.DataFrame(row)
df.columns = df.iloc[0]
df = df.reindex(df.index.drop(0))

x = list()
y = list()

for i in range(0,len(row)):
	for j in range(0,len(row[i])):
		if j == 0: 
			x.append(row[i][j])
		if j == 1: 
			y.append(row[i][j])

print(str(x))
print(str(y))