# Cluster-based approaches for cryptocurrency portfolio optimization (FIN-525 Final Project)
 
*Jeremy Di Dio & Robin Jaccard*

## Abstract

This paper conducts various filtering methods on the cross-correlation matrix of cryptocurrency returns, aiming to construct an optimal investment portfolio in the dynamic landscape of digital assets. Building on Markowitz's work, we focus on the estimation of correlation matrices. Recognizing the limitations of empirical cross-correlation matrices in real financial markets, we explore various filtering techniques using Random Matrix Theory, Thresholding, Minimum Spanning Tree, and Planar Maximally Filtered Graph. Additionally, correlation-based clustering procedures are incorporated to identify asset groups with correlated movements, enabling a well-balanced risk exposure. Finally, Principal Component Analysis (PCA) is employed on each cluster to identify $\textit{leading coins}$ that can be used to create a global minimum variance portfolio. Using hourly log-returns of 269 cryptocurrencies from the period 01/01/2021 to 31/12/2022, we assess the stability of identified clusters and conduct a comparative analysis of out-of-sample risks associated with the different filtering methods.

## Data

To reproduce or use this project, you need to download the necessary data from the following Google Drive [link](https://drive.google.com/drive/folders/1RS8QV8xgJCwM1xmk-p1us-QkBD5quABq?usp=sharing). Once downloaded, place the entire folder at the root of the project. The organization of the data is structured as follows:


```
.
├── processed
│   ├── clusterings
│   │   ├── clusters_baseline_720_24.pkl
│   │   ├── clusters_mst_720_24.pkl
│   │   ├── clusters_pmfg_720_24.pkl
│   │   └── clusters_thresh_720_24.pkl
│   ├── hourly_return.csv
│   ├── id_coins.csv
│   └── normalized_log_ret.csv
└── raw
    ├── aggregates
    │   ├── market_caps.csv
    │   ├── prices.csv
    │   └── volumes.csv
    ├── all_coins_by_mc_1.json
    ├── all_coins_by_mc_2.json
    └── batches
        ├── raw_market_caps_1.csv
        ├── raw_market_caps_2.csv
        ├── raw_market_caps_3.csv
        ├── raw_market_caps_4.csv
        ├── raw_market_caps_5.csv
        ├── raw_prices_1.csv
        ├── raw_prices_2.csv
        ├── raw_prices_3.csv
        ├── raw_prices_4.csv
        ├── raw_prices_5.csv
        ├── raw_volumes_1.csv
        ├── raw_volumes_2.csv
        ├── raw_volumes_3.csv
        ├── raw_volumes_4.csv
        └── raw_volumes_5.csv
```

## Dependencies

To ensure a seamless setup of the required environment, please refer to the requirements.txt file included in the project. You can install the necessary dependencies by running:
```console
pip install -r requirements.txt
```

This will install all the dependencies essential for running the code and reproducing the project's results.

## Code organization

Within the ```src``` directory, the ```scripts/data_downloader``` folder encapsulates the logic for retrieving data from CoinGecko through their API, while the ```loader/utils``` folder houses utility functions for batch aggregation. The notebooks directory contains the detailed ```Main.ipynb```, providing insights into the raw data processing and cluster creation processes. All datasets reside in the data folder, accessible via a Google Drive link outlined in the above section.

Here is an overview of the codebase:

```
.
├── LICENSE
├── README.md
├── data
│   └── ...
├── notebooks
│   ├── Analysis of the clusters.ipynb
│   ├── Asset_selection.ipynb
│   └── Main.ipynb
├── requirements.txt
└── src
    ├── __init__.py
    ├── loader
    │   └── utils.py
    └── scripts
        └── data_downloader.py
```





