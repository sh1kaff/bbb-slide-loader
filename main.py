import argparse
import os

from config import *
from download import download_slides

def _parse_arguments():
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="DownloadS slides from BBB"
    )

    parser.add_argument("url", type=str, help="URL like 'https://bbb123.ssau.ru/bigbluebutton/presentation/aa788..f9ed-173..849/aa78..f9ed-173..49/c41..34d-1..4/'")
    parser.add_argument("start", type=int, nargs="?", help="Start slide index.")
    parser.add_argument("end", type=int, nargs="?", help="End slide index.")
    
    return parser.parse_args()



if __name__ == "__main__":
    args = _parse_arguments()

    if not os.path.exists(OUTDIR):
        os.mkdir(OUTDIR)

    try:
        path_svg = download_slides(
            args.url, 
            (args.start, 1)[args.start is None], 
            args.end
        )
    except Exception as e:
        print(e)
        exit()

    print(f"Download to: {path_svg}")