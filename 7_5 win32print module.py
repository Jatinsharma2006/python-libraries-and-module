#Printing in Python
#pip install pywin32

import os, sys
import win32print as w32p

printer=str(w32p.GetDefaultPrinter())

# 1. Open the printer by name
p = w32p.OpenPrinter(printer)
try:
    # 2. Start the print job
    job = w32p.StartDocPrinter(p, 1, ("test of raw data", None, "RAW"))

    try:
        # 3. Start a new page
        w32p.StartPagePrinter(p)
        # 4. Send raw data to printer
        w32p.WritePrinter(p, b"data to print")
        # 5. End the current page
        w32p.EndPagePrinter(p)
    finally:
        # 6. End the document (very important!)
        w32p.EndDocPrinter(p)
finally:
    # 7. Close the printer connection
    w32p.ClosePrinter(p)
