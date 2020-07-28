import openpyxl

book = openpyxl.Workbook()

sheet = book.active
sheet.title = 'First sheet'

cells = sheet['A1':'B4']
i = 0

for row in cells:
    for cell in row:
        cell.value = i
        i += 1
cell2 = sheet['C1']
cell2.value = 'aaa'

book.save('demo.xlsx')
            