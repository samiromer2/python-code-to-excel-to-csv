# importe required libraries
import openpyxl
import csv
import pandas as pd

# open given workbook
# and store in excel object
excel = openpyxl.load_workbook("uploaded/current.xlsx")

# select the active sheet
sheet = excel.active

# writer object is created
col = csv.writer(open("csvfiles/current.csv",
					'w',
					newline=""))

# writing the data in csv file
for r in sheet.rows:
	# row by row write
	# operation is perform
	col.writerow([cell.value for cell in r])

# read the csv file and
# covert into dataframe object
df = pd.DataFrame(pd.read_csv("csvfiles/current.csv"))

# show the dataframe
df
