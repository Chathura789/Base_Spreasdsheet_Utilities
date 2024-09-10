import pandas as pd
import os

def combine_excel_files(folder_path):
    # Initialize an empty list to hold the dataframes
    df_list = []
    
    # Iterate over each file in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.xlsx'):
            file_path = os.path.join(folder_path, file_name)
            # Read the Excel file
            xls = pd.ExcelFile(file_path)
            
            # Iterate over each sheet
            for sheet_name in xls.sheet_names:
                # Read the sheet into a dataframe
                df = pd.read_excel(xls, sheet_name=sheet_name)
                # Add columns to identify the source sheet and tab
                df['source_tab'] = sheet_name
                df['source_sheet'] = file_name
                # Append the dataframe to the list
                df_list.append(df)
    
    # Concatenate all dataframes into a single dataframe
    combined_df = pd.concat(df_list, ignore_index=True)
    
    return combined_df

# Example usage
folder_path = 'your_folder_path'
combined_df = combine_excel_files(folder_path)
print(combined_df)
