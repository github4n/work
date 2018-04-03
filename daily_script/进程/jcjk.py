import psutil
# import xlsxwriter


PID = 20996
row = 60
# workbook = xlsxwriter.Workbook('flashreport.xlsx')
# worksheet = workbook.add_worksheet("测试总况")
# worksheet.write(0, 0, '时间(s)')
# worksheet.write(0, 1, 'cpu占比(%)')
# worksheet.write(0, 2, '内存(M)')
# 总cpu
cpucount = psutil.cpu_count(logical=True)
# 总内存
info = psutil.virtual_memory()
process = psutil.Process(int(PID))
cpuavg = 0
memoryavg = 0
for i in range(1, row + 1):
    cpupercent = process.cpu_percent(interval=1)
    memory = process.memory_info().rss / 1024 / 1024
    cpu = cpupercent / cpucount
    cpuavg = cpuavg + cpu
    memoryavg = memoryavg + memory
    print(i, cpu, memory)
    # worksheet.write(i, 0, i)
    # worksheet.write(i, 1, cpu)
    # worksheet.write(i, 2, memory)

# 图表10.48229166666666 253.7857421875
# chart1 = workbook.add_chart({'type': 'line'})
# chart1.add_series({
#     'name': 'CPU(%)',  # ['Sheet1', 0, 2]
#     'categories': [worksheet.name, 1, 0, row, 0],
#     'values': [worksheet.name, 1, 1, row, 1],
# })
# chart1.set_style(10)
# worksheet.insert_chart('D1', chart1, {'x_offset': 25, 'y_offset': 10})


# chart2 = workbook.add_chart({'type': 'line'})
# chart2.add_series({
#     'name': '内存(M)',  # ['Sheet1', 0, 2]
#     'categories': [worksheet.name, 1, 0, row, 0],
#     'values': [worksheet.name, 1, 2, row, 2],
# })
# chart2.set_style(10)
# worksheet.insert_chart('M1', chart2, {'x_offset': 25, 'y_offset': 10})

# workbook.close()
print(cpuavg / row, memoryavg / row)
