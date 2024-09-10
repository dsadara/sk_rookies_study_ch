from openpyxl import Workbook
from openpyxl import load_workbook

wb = load_workbook('excel_data1.xlsx')
sheet = wb.active
cell = sheet["A1":"C7"]

for row in cell:
    result = []
    for data in row:
        result.append(data.value)
    print(result)