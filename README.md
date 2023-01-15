# Team ChickenBurrito - Daisy Hackathon 2023
Solution by Team ChickenBurrito for Daisy Intelligence 2023 Hackathon

## Dataset
Online Retail II (ORII) dataset from UCI. Here is the [dataset description](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II).

The dataset was collected over 2 years, and consists of invoice records, products, and customer IDs.

Data prepreprocessing, including data cleaning and cancellation invoice resolution, is preformed on the raw dataset. 
The script `data_process.py` can be modified to suit other datasets.

[Supermarket Sales](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales) (SS) dataset from Kaggle which includes historical sales data of supermarket company recorded in 3 different branches for 3 months is also used to demostrate ARIMA forecasting. 

## Running Environment
Running environment for flyer generation is specified in `requirements.txt`. All other script can be run in Google Colab python environment.

## Running Instruction
Steps and example of outputs are shown in each `*.ipynb` files for different functions.
* `ORII_recommendation.ipynb`: collaborative filtering on ORII for product recommendation 
* `ORII_ARIMA_forecast.ipynb`: ARIMA forecast on quantity of goods sold for North American subset of ORII 
* `supermarket_ARIMA_forecast.ipynb`: ARIMA forecast on gross income for SS 
