import pandas as pd
from db.sql_server import connect_to_db, fetch_data
from validation.validator import validate_data
from export.excel_exporter import export_to_excel
from utils.helpers import log_error

def main():
    try:
        # Connect to the SQL Server database
        connection = connect_to_db()
        
        # Fetch data from the database
        data = fetch_data(connection)
        
        # Validate the fetched data
        if validate_data(data):
            # Export the validated data to Excel
            export_to_excel(data, 'output.xlsx')
        else:
            log_error("Data validation failed.")
    
    except Exception as e:
        log_error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()