#final desired data formats:
# - Charts:[["Test Name",<NumberOfAsserts>,<NumberOfFailedAsserts>],...]

import csv
from string import Template

test_data= []
with open('TestAnalysisData.csv') as test_analysis_file:
    file_reader = csv.reader(test_analysis_file)
    for row in file_reader:
        test_data.append(row)

chart = [['Test Name', 'Number of Assert', 'Number Failed Assert']]

for row in test_data[1:]:
    test_name = row[0]
    number_assert = int(row[1])
    failed_assert = int(row[2])
    chart.append([test_name, number_assert, failed_assert])

print (" Result ",chart)

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
<div id="chart_div" style="width:100%; height:600"></div>
</body>
</html>
""")

chart_data = ''
for row in chart[1:]:
    chart_data += '%s,\n'%row

completed_html = html_string.substitute(labels = chart[0], data = chart_data)

with open('testAssertResult.html', 'w') as f:
    f.write(completed_html)