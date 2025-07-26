import subprocess
from openpyxl import Workbook, load_workbook
from openpyxl.drawing.image import Image

input_file = "Automata.xlsx"
output_dir = "C:/Users/xthem/Documents"

wb = load_workbook(filename=input_file)
sheet_ranges = wb['Sheet1']
sheet_ranges['D3'].value = "LIDL"

wb.save(filename=input_file)


subprocess.run([
    r"C:\Program Files\LibreOffice\program\soffice.exe",
    "--headless",
    "--convert-to", "pdf:calc_pdf_Export:{\"Magnification\":{\"type\":\"long\",\"value\":\"4\"}, \"Zoom\":{\"type\":\"long\",\"value\":\"65\"}}",
    "--outdir", output_dir,
    input_file
])




'''
(usi automate)
nr contract E1
produs: D2
beneficiar: D3
locatie: D4
anul fabricatiei: D5
comanda nr: D6
nr: D7
Dimensiuni: D8
tip: D9 

prodous cap tabel: B12

check lipsuri serioase: B46
check informat: B47

data inspectie: D48
tehincian: D49
reprezentant beneficiar: D50

'''