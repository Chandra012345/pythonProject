import openpyxl
file="C:\\Users\\hp\\PycharmProjects\\pythontraining\\pythonProject3\\Day5\\WriteData.xlsx"
workbook=openpyxl.load_workbook(file)
sheet=workbook["Sheet1"]

for r in range(1,6):
    for c in range(1,4):
        sheet.cell(r,c).value="welcome"

workbook.save(file)





