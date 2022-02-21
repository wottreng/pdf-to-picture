import os
import time
from pdf2image import convert_from_path
from os import listdir
from os.path import isfile, join

start = time.time()

mypath = os.getcwd()
outpath = os.getcwd()
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for n in range(0, len(onlyfiles)):
    # get number of pages in each document
    if ".pdf" in onlyfiles[n][-4:]:
        print(f"[*] pdf found: {onlyfiles[n]} [*]")
        pages = convert_from_path(f"{mypath}/{onlyfiles[n]}")
        page_number = 1
        for page in pages:
            newFileName = onlyfiles[n].split(".")[0] + f"_{page_number}.png"
            page.save(f"{outpath}/{newFileName}", "png")
            print(f"{onlyfiles[n]}, page# {page_number} saved to {newFileName}")
            page_number += 1

print(f"** pdf to png function finished **\nfunction time: {round(time.time()-start,2)} seconds")
