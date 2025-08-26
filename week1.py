import kagglehub
from kagglehub import KaggleDatasetAdapter


###--- Week 1 Pands and Data handling ---###

###--- Day 1 - Intro to Python  + Set up ---###
import os
import pandas as pd
# from kaggle.api.kaggle_api_extended import KaggleApi

# Authenticate
# api = KaggleApi()
# api.authenticate()

# Download dataset (if not already downloaded)
dataset = "zynicide/wine-reviews"  # Example Kaggle dataset
path = "datasets"
# if not os.path.exists(path):
#     os.makedirs(path)

# api.dataset_download_files(dataset, path=path, unzip=True)

# Load into Pandas
csv_file = os.path.join(path, "winemag-data_first150k.csv")
df = pd.read_csv(csv_file)

# print(df.head())
def day1():
    print("First 5 records:", df.head())
    print("Column information:", df.info())
    print("descriptive statistics:", df.describe())

#for this sample, we installed kaggle and got the data set there
#we then load the data, loading it via csv or google sheets will be different but same concept
# we then displayed head or the first few rows of the code, and info, and describe to get some statistical values

###--- ---###
###--- Day 2 – Selecting Data (Rows/Columns) ---###
def day2(): 
    Country_Col = df["country"]
    US_winery = df[df["country"] == "US"] #select Rows is US
    print(Country_Col)
    print(US_winery)



###--- Day 3 – Basic Operations ---###
#Colmns = country,description,designation,points,price,province,region_1,region_2,variety,winery
def day3(): 
    print(df.describe()) #get the statistic description
    print(df.variety.value_counts()) #for gender, .nunique() for test scores
    print(df.variety.value_counts(normalize=True))
    print(df.province.nunique())
    print()


###--- Day 4 – Sorting and Renaming ---###
def day4():
    print(df.sort_values(by=['country','price']))
    df2=df.rename(columns={'country': 'bansa'})
    print(df2)

def day5():
    na_bool_values = df.isna()
    print(na_bool_values)
    med_price = df["price"].median
    df["price"] = df["price"].fillna(med_price)
    print(df['price'])

def day6():
    country_g = df.groupby("country").agg({"points":'sum',"price":'sum'})
    country_g["price/point"] = country_g["price"]/country_g["points"]
    print(country_g)

