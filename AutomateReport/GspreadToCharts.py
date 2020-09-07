import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('clientSecret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('TestRunData').sheet1


#read in the data from the spreadsheet
spreadsheet_data = sheet.get_all_values()

run_times = []
for row in spreadsheet_data:
    del row[0]
    del row[1]
    run_times.append(row)


#read in csv data
csv_data = []
with open('LatestTestRunData.csv') as test_data_csv:
    file_reader = csv.reader(test_data_csv)
    for row in file_reader:
        csv_data.append(row)


run_date = csv_data[1][2]
#now get the first row of the run_times list and modify it to remove the oldest value
spreadsheet_header_row = run_times[0]
spreadsheet_header_row.append(run_date)
del spreadsheet_header_row[0]
#and add in the new run date
for spreadsheet_row,csv_row in zip(run_times[1:], csv_data[1:]):
    new_value = csv_row[1]
    spreadsheet_row.append(new_value)
    del spreadsheet_row[0]


#write the new spreadsheet data back into the spreadsheet
for row_index,row in enumerate (run_times):
    for col_index, cell in enumerate(row):
        sheet.update_cell(row_index+1, col_index+3, cell)


#read in the average data from the spreadsheet
#Hint: use sheet.col_values
avg_data = sheet.col_values(2)

#intializing the chart_data list with the headers
chart_data = [["Test Name","Diff From Avg"]]
for avg,current in zip (avg_data[1:], csv_data[1:]):
    diff = float(avg)-float(current[1])
    chart_data.append([current[0], diff])


from string import Template
#first substitution is the header, the rest is the data
htmlString = Template("""<html><head><script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);
  
  function drawChart(){
      var data = google.visualization.arrayToDataTable([
      $labels,
      $data
      ],
      false);

      var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data);
  }
</script>
</head>
<body>
<div id = 'chart_div' style='width:800; height:600'><div>
</body>

</html>""")

#format the data correctly
chart_data_str = ''
for row in chart_data[1:]:
    chart_data_str += '%s,\n'%row

#Substitute the data into the template
completed_html = htmlString.substitute(labels = chart_data[0], data = chart_data_str)

#Write the html to a file
with open('chart.html','w') as f:
    f.write(completed_html)
