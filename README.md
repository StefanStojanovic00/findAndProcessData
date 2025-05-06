# 📊 Excel Table Data Filler

This Python project automates the process of transferring and filling in missing data from one Excel spreadsheet into another. It uses `pandas` and `openpyxl` to handle Excel files and perform data manipulation.

## 📝 Description

You have two Excel files:
- **Source Table**: Fully populated with data.
- **Target Table**: Partially filled or missing values.

The script reads both tables and intelligently fills in the missing data in the target table by using matching information from the source table.

## 🚀 Features

- Load and process `.xlsx` files
- Match and fill missing data from source to target table
- Preserve Excel formatting when possible
- Includes a basic test to verify functionality

## 📦 Technologies Used

- [pandas](https://pandas.pydata.org/) – Data analysis and manipulation
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/) – Read/write Excel 2010 xlsx/xlsm files


