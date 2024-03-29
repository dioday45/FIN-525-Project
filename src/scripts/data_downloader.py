"""
Download data from CoinGecko API

Usage: 
data_downloader.py --data=<path> --batch=<int>

Options:
    --data=<path>   Path to the data folder
    
"""


import csv
from tqdm import tqdm
import requests
import time
import pandas as pd
from docopt import docopt
from pathlib import Path
import datetime
import numpy as np


def main(data_src: Path, batch: int):
    with open((data_src / "id_coins.csv"), newline="") as f:
        reader = csv.reader(f)
        coins_id = list(reader)[0]

    # Split the list of coins in batches of 100
    coins_id = coins_id[batch * 100 - 100 : batch * 100]

    data = {"vs_currency": "usd", "days": "max"}
    count = 0

    p = pd.DataFrame()
    v = pd.DataFrame()
    m = pd.DataFrame()

    for id in tqdm(coins_id):  # For each asset ID
        START = datetime.datetime(2020, 1, 2)  # Start getting data from the 02.01.2020
        END = datetime.datetime(2023, 1, 2)  # Getting data up to the 02.01.2023

        current = START
        count = 0
        prices = []
        volumes = []
        market_caps = []

        time.sleep(40)  # Ensure to not reach number of requests time limit

        while current < END:
            if count >= 6:
                time.sleep(40)  # Ensure to not reach number of requests time limit
                count = 0

            _from = current
            _to = current + datetime.timedelta(days=90)  # Move to the following 90 days
            data = {
                "vs_currency": "usd",
                "from": _from.timestamp(),
                "to": _to.timestamp(),
            }
            url = f"https://api.coingecko.com/api/v3/coins/{id}/market_chart/range"

            try:
                # Get data from API
                response = requests.get(url, params=data)
                prices += response.json()["prices"]
                volumes += response.json()["total_volumes"]
                market_caps += response.json()["market_caps"]
                current = _to
                count += 1
            except Exception as e:
                print(e)
                time.sleep(60)
                continue

        # Save data in a dataframe
        price_df = pd.DataFrame(
            prices,
            columns=["date", id],
            index=[pd.to_datetime(x[0], unit="ms") for x in prices],
        ).drop(columns=["date"])
        volume_df = pd.DataFrame(
            volumes,
            columns=["date", id],
            index=[pd.to_datetime(x[0], unit="ms") for x in volumes],
        ).drop(columns=["date"])
        market_cap_df = pd.DataFrame(
            market_caps,
            columns=["date", id],
            index=[pd.to_datetime(x[0], unit="ms") for x in market_caps],
        ).drop(columns=["date"])

        # Concatenate dataframes
        p = pd.concat([p, price_df], axis=1)
        v = pd.concat([v, volume_df], axis=1)
        m = pd.concat([m, market_cap_df], axis=1)

    # Save dataframes
    p.to_csv(data_src / f"raw_prices_{batch}.csv")
    v.to_csv(data_src / f"raw_volumes_{batch}.csv")
    m.to_csv(data_src / f"raw_market_caps_{batch}.csv")


if __name__ == "__main__":
    args = docopt(__doc__)
    data_src = Path(args["--data"])
    batch = int(args["--batch"])
    main(data_src, batch)
