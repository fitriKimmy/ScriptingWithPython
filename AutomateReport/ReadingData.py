# Provide data with these format from file provided
# data1 [[Test name, different from average runtime]]
# data2 [[Test name, current run time]]

import csv

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

print("Result 1 ", data1)
print("Result 2", data2)