from openpyxl import Workbook
from openpyxl import load_workbook

wb = load_workbook('excel_data2.xlsx', data_only=True) # data_only 수식 포함
sheet = wb.active
cell = sheet["A1":"E7"]

for row in cell:
    result = []
    for data in row:
        result.append(data.value)
    print(result)