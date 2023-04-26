import os
import requests
import matplotlib.pyplot as plt
import time
import numpy as np
import pandas as pd
import re

def downloadFile():

    URL = r'https://sdw-wsrest.ecb.europa.eu/service/data/YC/B.U2.EUR.4F.G_N_A+G_N_C.SV_C_YM.?lastNObservations=1&format=csvdata'
    DOWNLOAD_FILE = "latest_spot_rate_data.csv"

    current_time = time.time()
    status = os.path.getmtime(DOWNLOAD_FILE)

    seconds_till_update = 86400
    if (status and current_time - status >= seconds_till_update):
        with open(DOWNLOAD_FILE, "wb") as f:
            f.write(requests.get(URL).content)

    return DOWNLOAD_FILE

def sort(array, kind='mergesort'):
    return np.sort(array, kind=kind)


def main():

    DOWNLOAD_FILE = downloadFile()
    df = pd.read_csv(DOWNLOAD_FILE)

    keys = df['KEY']
    data_type = "DATA_TYPE_FM"
    all_bonds = "G_N_C"

    ttm_aaa = []
    val_aaa = []
    ttm_all = []
    val_all = []

    for key in keys:

        sr = df.loc[keys == key, 'DATA_TYPE_FM'].values[0]

        if (sr.startswith("SR_")):
            years, months = 0,0

            dates = re.findall(r'\d+', sr)

            if (len(dates) == 1):
                if ("Y" in sr):
                    years = dates[0]
                else:
                    months = dates[0]
            else:
                years, months = dates

            time = int(years) + int(months) / 12.0
            val = df.loc[keys == key, 'OBS_VALUE'].values[0]

            if (all_bonds in key):
                val_all.append(val)
                ttm_all.append(time)
            else:
                val_aaa.append(val)
                ttm_aaa.append(time)    


    """
    As values are always increasing,
    they are sorted to be able to plot without scatter
    """ 

    ttm_aaa = sort(ttm_aaa)
    val_aaa = sort(val_aaa)

    ttm_all = sort(ttm_all)
    val_all = sort(val_all)

    plt.scatter(ttm_aaa, val_aaa, label='AAA bond')
    plt.scatter(ttm_all, val_all, label='All bonds')
    plt.xlabel('Maturity (years)')
    plt.ylabel('Yield (%)')
    plt.title('Yield Curve (AAA bonds and All bonds)')
    plt.legend()
    plt.show()

main()
