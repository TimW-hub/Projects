# Takes the PDFS exctracted from online and converts to CSV for further manipulation
# Second task in list to make sorting faster computationally, and may be paired with extraction process
# Extra
# Check at this step if conversion was successful and seperate out failed csvs w/ reference PDFS
# https://www.temukasales.co.nz/sales/past?r=10

# Seperated by type of cattle
# Monday/Thursdays standard dates
# fresian maybe to be seperated out
# Date
# Tally
# DESCRIPTION
# Kg 
# $/Head 
# $/kg 


# identify outlyer table types such as non-cattle reports (commonly EWE reports)
# and weekly reports which should be seperated from the main data (df stands for dataframe)

def table_type_identify(pdf_output):
    '''Seperates imported PDFs by table style and removes data about unwanted animals
        Table List object input (from Camelot module pdf reading)
        OUTPUT: String for unhandled format OR List of DataFrames on standard format discovery'''
    df_out = []
    for table in pdf_output:
        df = table.df

        # singling out weekly reports 2 typical signs of a weekly report which are never used in sales reports
        report_substring = "report"
        report_check = df.applymap(lambda x: report_substring in x.lower()).to_numpy()
        df_dimensions = df.shape[1]
        if df_dimensions <= 6 or True in report_check:
            return "Weekly-Report"

        # removing ewe reports (common other type of non-cattle report,
        # also featured in weekly reports so used as a secondary catch method)
        ewe_substring = "ewe"
        ewe_check = df.applymap(lambda x: ewe_substring in x.lower()).to_numpy()
        if True in ewe_check:
            return "Ewe"

        df_out.append(df)
    # if for loop completes return confirmation that re
    return df_out

def table_format(df_tables):
    '''Takes PDF outputs and converts to ideal CSV column layout,
        cleans up data within table and removes unecessary rows on a per document basis
        OUTPUT: Formatted DataFrame'''

    #identify key columns and remove rest
    #check data in rows is correct and has not moved before deleting
    #insert date column at the start 2nd column (after index)
    #Clean up element data random spaces or /n or other oddities
    #remove rows with empty data and title rows (possibly change to titles to index)


def combine_tables(formatted_table_list):
    '''Combine all tables from an input LIST with the assumption they are formatted correctly,
    If formatting not possible error to be sent
    OUTPUT: Single DataFrame'''

    #combined table list
    #error handling


import os
from os.path import isfile, join
import camelot
import shutil
import pandas as pd
import numpy as np

DOWNLOAD_DIR = "downloaded_pdfs/"
EXPORT_DIR = "csv_files/"
EXPORT_WEEKLY_DIR = "csv_files/weekly_sales/"

files_list = os.listdir(DOWNLOAD_DIR)

# PDF file extracted
for file in files_list:
    if isfile(join(DOWNLOAD_DIR, file)):
        file_csv = file.rstrip("pdf") + "csv"
        # create a table list from the document
        table_list = camelot.read_pdf(f"{DOWNLOAD_DIR}{file}", flavor="stream", pages="all")
        df_tables = table_type_identify(table_list)
        # print(df_tables)

        if df_tables == "Ewe":
            os.remove(f"{DOWNLOAD_DIR}{file}")
            print("Ewe report removed")
            break
        elif df_tables == "Weekly-Report":
            table_list.export(f"{EXPORT_WEEKLY_DIR}{file_csv}", f="csv")
            # os.remove(f"{DOWNLOAD_DIR}{file}")
            print("Weekly report exported to seperate folder 'weekly-reports'")
            break 

        

        # file_csv = "2022-04-13-v2.csv"
        # tables.export(f"{EXPORT_DIR}{file_csv}", f="csv")


        
# print(tables[0].df)
# print(tables[1].df)
