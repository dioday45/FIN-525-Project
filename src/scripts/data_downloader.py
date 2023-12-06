"""
Download data from CoinGecko API

Usage: 
data_downloader.py --data=<path>

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


def main(data_src: Path):
    with open((data_src / "id_coins.csv"), newline="") as f:
        reader = csv.reader(f)
        coins_id = list(reader)[0]

    data = {"vs_currency": "usd", "days": "max"}
    headers = {"Content-type": "application/json"}
    count = 0

    prices = pd.DataFrame()
    volumes = pd.DataFrame()
    market_caps = pd.DataFrame()

    for id in tqdm(coins_id):
        if count == 5:
            time.sleep(60)
            count = 0

        url = f"https://api.coingecko.com/api/v3/coins/{id}/market_chart"
        response = requests.get(url, headers=headers, params=data)
        count += 1

        try:
            index = [pd.to_datetime(x[0], unit="ms") for x in response.json()["prices"]]
            prices = pd.concat(
                [
                    prices,
                    pd.DataFrame(
                        data=[x[1] for x in response.json()["prices"]],
                        index=index,
                        columns=[id],
                    ),
                ],
                axis=1,
            )
            volumes = pd.concat(
                [
                    volumes,
                    pd.DataFrame(
                        data=[x[1] for x in response.json()["total_volumes"]],
                        index=index,
                        columns=[id],
                    ),
                ],
                axis=1,
            )
            market_caps = pd.concat(
                [
                    market_caps,
                    pd.DataFrame(
                        data=[x[1] for x in response.json()["market_caps"]],
                        index=index,
                        columns=[id],
                    ),
                ],
                axis=1,
            )

        except Exception as e:
            print(e, response.json())
            break

    prices.to_csv(data_src / "prices.csv")
    volumes.to_csv(data_src / "volumes.csv")
    market_caps.to_csv(data_src / "market_caps.csv")


if __name__ == "__main__":
    args = docopt(__doc__)
    data_src = Path(args["--data"])
    main(data_src)
