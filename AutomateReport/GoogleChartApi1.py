# Provide data with these format from file provided
# data1 [[Test name, different from average runtime]]
# data2 [[Test name, current run time]]

import csv
from string import Template


timing_data = []
with open('TestTimingData.csv') as test_timing_file:
    file_reader = csv.reader(test_timing_file)
    for row in file_reader:
        timing_data.append(row)

data1 = [['Test Name', 'Diff from average']]
data2 = [['Test Name', 'Current run time']]

for row in timing_data[1:]:
    test_name = row[0]
    if not row[1] or not row[2]:
        continue
    current_run_time = float(row[1])
    avg_run_time = float(row[2])
    diff_run_time = avg_run_time - current_run_time
    data1.append([test_name, diff_run_time])
    data2.append([test_name, current_run_time])

html_string = Template("""
<html>
<head>
<script src="https://www.gstatic.com/charts/loader.js"></script>
<script>
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);

  function drawChart() {
      var data = google.visualization.arrayToDataTable([
       $labels,
       $data
      ],
      false); // 'false' means that the first row contains labels, not data.
  
      // Instantiate and draw our chart, passing in some options.
      var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data);
  }
</script>
</head>
<body>
<div id="chart_div" style="width:800; height:600"></div>
</body>
</html>""")

chart_data = ''
for row in data1[1:]:
    chart_data += '%s,\n'%row

completed_html = html_string.substitute(labels = data1[0], data = chart_data)

with open('diffAvgResult.html','w') as f:
    f.write(completed_html)