# Aim is to rework this so that CSV files (rather than PDFS currently) are handled here and sorted
# Final result is Categorized CSV files by format type
# Types: Store cattle // Store Cattle 10 column reports // Weekly reports // Non-cattle farm animals (to be cleared/removed)


import os
from os.path import isfile, join
import shutil
import camelot

DOWNLOAD_DIR = "downloaded_pdfs/"
# PATH_A = "downloaded_pdfs/weekly_reports/"
# PATH_B = "downloaded_pdfs/store_cattle_reports/"
# PATH_C = "downloaded_pdfs/store_cattle_reports_10col/"
# PATH_D = "downloaded_pdfs/misc_reports/"

tables = camelot.read_pdf(f"{DOWNLOAD_DIR}{file}", flavor="stream", pages="all")






# for file in files_list:
#     if isfile(join(STARTING_DIR, file)):
#         tables = camelot.read_pdf(f"{STARTING_DIR}{file}", pages="all")
        
#         try:
#             if any(["Cattle Sale" in tables[0].data[0][0],
#                     "Calf" in tables[0].data[0][0],
#                     "Friesian" in tables[0].data[0][0]]):
#                 shutil.move(f"{STARTING_DIR}{file}", f"{PATH_C}{file}")
#                 print(f"pdf moved: {file}")
#             elif any(["Cattle Sale" in tables[0].data[1][2],
#                     "Calf" in tables[0].data[1][2],
#                     "Friesian" in tables[0].data[1][2]]):
#                 shutil.move(f"{STARTING_DIR}{file}", f"{PATH_B}{file}")
#                 print(f"pdf moved: {file}")
#             elif tables[1].page == 1:
#                 shutil.move(f"{STARTING_DIR}{file}", f"{PATH_A}{file}")
#                 print(f"pdf moved: {file}")
#             elif "Ewe" in tables[0].data[1][2]:
#                 os.remove(f"{STARTING_DIR}{file}")
#                 print("Ewe spreadsheet deleted")
#             else:
#                 shutil.move(f"{STARTING_DIR}{file}", f"{PATH_D}{file}")
#                 print(f"ID failed sent to misc_reports.")
#         except:
#             shutil.move(f"{STARTING_DIR}{file}", f"{PATH_D}{file}")
#             print(f"ID failed sent to misc_reports.")

# #test
# file = "2018-11-22.pdf"
# tables = camelot.read_pdf(f"{STARTING_DIR}{file}", pages="all")
# print(tables)
# print(tables[0])
# # print(tables[1].data)
# print(tables[0].data[0:3])