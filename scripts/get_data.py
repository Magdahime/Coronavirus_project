import sys
import os
import requests, pathlib

def retrieve(sourceFile, name, destinationFolder):
    
    r = requests.get(sourceFile)
    assert r.status_code == requests.codes.ok
    with open(destinationFolder + f"/{name}","w+") as f:
        f.write(r.text)
    
retrieve("https://raw.githubusercontent.com/rambaut/MERS-Cases/gh-pages/data/cases.csv", "mers.csv", "raw_data")