import sys
import os
import re
import requests, pathlib
import pandas as pd

def retrieve(sourceFile, name, destinationFolder):
    df = pd.DataFrame()
    r = requests.get(sourceFile)
    assert r.status_code == requests.codes.ok
    with open(destinationFolder + f"/{name}","w+") as f:
        f.write(r.text)
    df = pd.read_csv(destinationFolder + f"/{name}", error_bad_lines=False)
    return df


def get_name(url):
    result = re.search("data_[a-z]*\.csv", url)
    return url[result.start():]
