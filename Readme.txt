# Combine Excel Files

This project provides functions to combine all tabs from all spreadsheets in a given folder into a single DataFrame. The functions are available in both Python and R. Each row in the resulting DataFrame includes two identifier columns: `source_tab` (the tab in the spreadsheet where the record came from) and `source_sheet` (the file where the record came from).

## Python

### Function: `combine_excel_files`

This function reads all the Excel files in the specified folder, adds columns to identify the source sheet and tab, and combines the data into a single DataFrame.

#### Usage

1. Ensure you have `pandas` installed:
    ```bash
    pip install pandas
    ```

2. Use the function in your script:
    ```python
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
    ```

## R

### Function: `combine_excel_files`

This function reads all the Excel files in the specified folder, adds columns to identify the source sheet and tab, and combines the data into a single DataFrame.

#### Usage

1. Ensure you have `readxl` and `dplyr` installed:
    ```r
    install.packages("readxl")
    install.packages("dplyr")
    ```

2. Use the function in your script:
    ```r
    library(readxl)
    library(dplyr)

    combine_excel_files <- function(folder_path) {
      # Initialize an empty list to hold the dataframes
      df_list <- list()
      
      # Get the list of files in the folder
      files <- list.files(folder_path, pattern = "\\.xlsx$", full.names = TRUE)
      
      # Iterate over each file
      for (file_path in files) {
        # Get the sheet names
        sheet_names <- excel_sheets(file_path)
        
        # Iterate over each sheet
        for (sheet_name in sheet_names) {
          # Read the sheet into a dataframe
          df <- read_excel(file_path, sheet = sheet_name)
          # Add columns to identify the source sheet and tab
          df <- df %>% mutate(source_tab = sheet_name, source_sheet = basename(file_path))
          # Append the dataframe to the list
          df_list[[paste(basename(file_path), sheet_name, sep = "_")]] <- df
        }
      }
      
      # Bind all dataframes into a single dataframe
      combined_df <- bind_rows(df_list)
      
      return(combined_df)
    }

    # Example usage
    folder_path <- 'your_folder_path'
    combined_df <- combine_excel_files(folder_path)
    print(combined_df)
    ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
