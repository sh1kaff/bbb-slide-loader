import os
import requests
from secrets import token_hex

from config import *

def download_slides(url: str, start: int = 1, end: int = None) -> str:
    url = os.path.join(url, "svg/", "{index}")
    
    index = start

    while True:
        dirname = os.path.join(OUTDIR, f"slides_{token_hex(nbytes=3)}")

        if os.path.exists(dirname): 
            continue
        
        os.mkdir(dirname)
        break


    while True:
        if end is not None and index == end + 1:
            break
        
        res = requests.get(url.format(index=index), stream=True, timeout=5)

        if res.status_code == 404:
            break

        filename = os.path.join(dirname, f"slide_{index}.svg")
        print(filename)
        with open(filename, "wb") as file:
            for chunk in res:
                file.write(chunk)

        index += 1
    
    return dirname