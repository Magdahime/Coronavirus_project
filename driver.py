import sys
import os 
import pandas as pd
sys.path.append(os.path.abspath('scripts'))
import get_data as gd
import formatting_data as fd

def main():
    data_frames ={}
    for arg in sys.argv[1:]:
        data_frames[gd.get_name(arg)] = gd.retrieve(arg, gd.get_name(arg), "raw_data")
        for df in data_frames:
            print(data_frames[df])

main()