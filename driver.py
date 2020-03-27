import sys
import os 
import pandas as pd
sys.path.append(os.path.abspath('scripts'))
import get_data as gd
import formatting_data as fd

def main():
    data_frames ={}
    #GETTING DATA FRAMES
    for line in open("scripts/urls.txt"):
        line = line[:-1]
        data_frames[gd.get_name(line)] = gd.retrieve(line, gd.get_name(line), "raw_data")
    #FORMATTING AND GRAPHING
    keys_list = data_frames.keys()
    fd.format_corona((data_frames[gd.get_key(keys_list, "coronacases")], data_frames[gd.get_key(keys_list, "coronadeaths")]))
    fd.format_sars(data_frames[gd.get_key(keys_list, "sars")])
    fd.format_swine_flu(data_frames[gd.get_key(keys_list, "swine")])

main()