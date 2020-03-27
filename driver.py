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
    #GETTING KEYS
    keys_list = data_frames.keys()
    key_corona1 = gd.get_key(keys_list, "coronacases")
    key_corona2 = gd.get_key(keys_list, "coronadeaths")
    key_swine = gd.get_key(keys_list, "swine")
    key_sars = gd.get_key(keys_list, "sars")
    #GRAPHING FOR EACH DISEASE
    #fd.format_corona((data_frames[key_corona1], data_frames[key_corona2]))
    #fd.format_sars(data_frames[key_sars])
    #fd.format_swine_flu(data_frames[key_swine])
    #GRAPHING TOGETHER
    fd.gather_data(((data_frames[key_corona1], data_frames[key_corona2])),
                   data_frames[key_sars],data_frames[key_swine])
    

main()