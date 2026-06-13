import xlwings as xw
import os
import pandas as pd

# Define the input and output directories
input_dir = "../data"
output_dir = "../data"

# List all .xls files in the input directory
xls_files = [f for f in os.listdir(input_dir) if f.endswith('.xls')]

# Create an empty dataframe to hold all the data
combined_data = pd.DataFrame()

# Loop through each file and append its content to the combined dataframe
for file in xls_files:
    file_path = os.path.join(input_dir, file)
    
    try:
        # Use xlwings to open the file and read the data
        with xw.App(visible=False) as app:
            workbook = app.books.open(file_path)
            sheet = workbook.sheets[0]
            data = sheet.range('A1').expand().value  # Get all data from the sheet
            df = pd.DataFrame(data[1:], columns=data[0])  # Convert to DataFrame
            combined_data = pd.concat([combined_data, df], ignore_index=True)
    except Exception as e:
        print(f"Error reading {file}: {e}")
        continue

# Define the output file path
output_file = os.path.join(output_dir, 'combined_RAST.csv')

# Save the combined data to a .csv file
combined_data.to_csv(output_file, index=False)

print(f"Files have been combined into '{output_file}'.")
