import  xlsxwriter
from  xlsxwriter.utility import xl_rowcol_to_cell
from xlsxwriter.utility import xl_cell_to_rowcol ,xl_range_abs
wb = xlsxwriter.Workbook("text.xlsx")
# ....................
#it will convert row and col to A1,A2 etc
print(xl_rowcol_to_cell(0,0)) 

# .........................
# it will convert position A1 to row (0,0) 
print(xl_cell_to_rowcol("A1 ")) 

# .............................
# it will convert this range to $A$1:$L$12
print(xl_range_abs(0,0,11,11)) 

# ............................

#create a tab in xlsx under

ws = wb.add_worksheet("tab")
   
#write in the worksheet 

ws.write(0,0,"hellow world")   
ws.write(0,2,1)
ws.write(1,2,2)
#..........................

# Arithmetic Operation

ws.write(2,2,'=Sum(C1:C2)')

wb.close()
