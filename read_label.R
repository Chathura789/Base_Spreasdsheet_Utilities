# Load necessary libraries
library(readxl)
library(purrr)
library(dplyr)

# Define the folder path
folder_path <- "path/to/your/folder"

# List all Excel files in the folder
file_list <- list.files(path = folder_path, pattern = "*.xlsx", full.names = TRUE)

# Function to read data from each file and add source columns
read_and_label <- function(file) {
  sheets <- excel_sheets(file)
  map_dfr(sheets, ~ {
    data <- read_excel(file, sheet = .x)
    data %>%
      mutate(Source_File = basename(file), Source_Sheet = .x)
  })
}

# Use map to read and combine all data
master_table <- map_dfr(file_list, read_and_label)

# Print the master table
print(master_table)
