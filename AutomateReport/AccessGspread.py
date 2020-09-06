import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
credential = ServiceAccountCredentials.from_json_keyfile_name('clientSecret.json', scope)
client = gspread.authorize(credential)

sheet = client.open('ServiceAccountTest').sheet1
# 5,5,test - means row 1 column 1, add string test
sheet.update_cell(5,5,'test') 

#Get all values from gspread
print(sheet.get_all_values())

# 3 columns with each contains 2 rows
# for in list start with 0 but in spread sheet row start from 1
my_data = [[1,2,3], [4,5,6]]
for row_index,row in enumerate(my_data):
    for column_index,value in enumerate(row):
        sheet.update_cell(row_index+1, column_index+1, value)