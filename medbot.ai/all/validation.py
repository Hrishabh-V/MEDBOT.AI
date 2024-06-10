
cond=input("enter your conditions: ")
print(cond)





# Load the Excel workbook
workbook = openpyxl.load_workbook('data.xlsx')

# Get the active sheet
sheet = workbook.active

# Define lists for the first and second columns
column1_values = []
column2_values = []

# Loop through each row in the sheet and append the first and second column values to the lists
for row in sheet.iter_rows(min_row=2, values_only=True):
    column1_values.append(row[0])
    column2_values.append(row[1])
    
    
for i  in range(len(column1_values)):
    if cond in column1_values[i]:
        print(column2_values[i])
        print(" ")
        


