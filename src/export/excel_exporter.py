from openpyxl import Workbook

def export_to_excel(data, file_name):
    if not data:
        raise ValueError("No data provided for export.")
    
    workbook = Workbook()
    sheet = workbook.active

    # Write header
    headers = data[0].keys()
    sheet.append(headers)

    # Write data rows
    for row in data:
        sheet.append(row.values())

    # Save the workbook
    workbook.save(file_name)