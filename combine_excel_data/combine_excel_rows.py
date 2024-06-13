import openpyxl
def combine_values(file_path): # leave as is
    wb = openpyxl.load_workbook(file_path) # leave as is
    sheet = wb.active
    # column AE based on column A values
    column_ae_values = {}
    
    # column A to find matches from column AE
    for row in sheet.iter_rows(min_row=2, values_only=True):  # assuming you have a header row
        column_a_value = row[0]  # get value from column A
        ae_value = row[30]  # assuming column AE is at index 30 (0-based index) // change index as needed
        if column_a_value not in column_ae_values:
            column_ae_values[column_a_value] = [ae_value]
        else:
            column_ae_values[column_a_value].append(ae_value)
    for key, values in column_ae_values.items():
        combined_ae_values = ', '.join(str(val) for val in values)
        print(f"Column A: {key}; Column AE: {combined_ae_values}")
excel_file_path = "your/path/here"
combine_values(excel_file_path)
