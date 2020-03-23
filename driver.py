import sys
import os 
import pandas as pd
sys.path.append(os.path.abspath('scripts'))
from get_data import retrieve

retrieve('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv', "data_corona.csv", "raw_data")
df = pd.read_csv("raw_data/data_sars.csv", error_bad_lines=False)
print(df)