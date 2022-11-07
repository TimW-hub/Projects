# Handles the URL download extraction process and saves to folder as PDFS
# Last updated 10/06/2022 - Tim Williams
# Comments: Optimization to be improved, to be incorperated with Tkinter interface with customizable date range, currently static (line 87)

from urllib.error import HTTPError
import urllib.request

def download_range(start_date, end_date):
    date = convert_to_int(start_date.split("/")) # date is now an integer array [day, month, year]
    end_date= convert_to_int(end_date.split("/"))
    date_range = round((end_date[2]-date[2])*365.25 + (end_date[1]-date[1])*30.45 + (end_date[0]-date[0]) + 1) # approximate length of loop iterations

    for x in range(date_range):
        if date[1] < 10:
            if date[0] < 10:
                filename = f"{date[2]}-0{date[1]}-0{date[0]}"
            else:
                filename = f"{date[2]}-0{date[1]}-{date[0]}"
            filename_alt = f"{date[2]}-0{date[1]}-{date[0]}"
        else:
            if date[0] < 10:
                filename = f"{date[2]}-{date[1]}-0{date[0]}"
            else:
                filename = f"{date[2]}-{date[1]}-{date[0]}"
            filename_alt = f"{date[2]}-{date[1]}-{date[0]}"
        
        pdf_path = f"https://www.temukasales.co.nz/store/doc/Sale-Report-{filename}.pdf"
        pdf_path_alt = f"https://www.temukasales.co.nz/store/doc/Sale-Report-{filename_alt}.pdf"
        pdf_path_alt_b = f"https://www.temukasales.co.nz/store/doc/sales-report-{filename}.pdf"
        
        result = download_file(pdf_path, filename, x, date_range)
        if not result[0]:
            download_file(pdf_path_alt, filename, x, date_range)
            if not result[0]:
                download_file(pdf_path_alt_b, filename, x, date_range)
        
        if result[1]:
            break

        date = new_date_assignment(date)

def convert_to_int(date):
    date[0] = int(date[0])
    date[1] = int(date[1])
    date[2] = int(date[2])
    return date

def new_date_assignment(date): # handles dates and when to reset numbers
    if any([date[1] == 2 and date[0] == 28,
            date[1] in [1,3,5,7,8,10,12] and date[0] == 31,
            date[1] in [4,6,9,11] and date[0] == 30]):
        days_reset(date)
    else:
        date[0] += 1
    return date

def days_reset(date): #sets dates back to 1st day of new month/year
    date[0] = 1
    if date[1] == 12:
        date[1] = 1
        date[2] += 1
    else:
        date[1] += 1
    return date

def download_file(download_url, filename,x,date_range): #downloads pdfs and places into "downloaded_pdfs" directory
    SUB_DIRECTORY = "downloaded_pdfs"
    download_successful = False
    exit_loop = False

    try: #handle file downloads with two filename options and count 404 errors, notify of other errors (404 errors expected on 95% of the date range)
        response = urllib.request.urlopen(download_url)
        file = open(SUB_DIRECTORY + "/" + filename + ".pdf", 'wb')
        file.write(response.read())
        file.close()
    except HTTPError:
        download_successful = False
    except:
        print("Something else went wrong...")
        exit_loop = True
    else:
        download_successful = True
        print(f"Progress: {x}/{date_range}. File successful for date: {filename}")

    return [download_successful, exit_loop]

download_range("21/3/2019", "1/1/2022")
print("Downloads complete.")