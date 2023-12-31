# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 10:57:59 2023
Dataset description : This dataset include historical data of flight delays. the objective is to investigate the flight delays factors.

➡ Dataset link


 

Instructions
Part 1: Data Exploration with Pandas
Load the provided dataset into a pandas dataframe
Use pandas to explore the dataset. For example, you might start by using the head() and info() methods to get an overview of the data.
Look for missing values in the dataset. You can use the isnull() method to identify missing values.
Use pandas to calculate some summary statistics for the dataset. For example, you might use the describe() method to get summary statistics for the numerical columns in the dataset.
Part 2: Data Exploration with ydata-Profiling
Use ydata-profiling to generate a report of the provided dataset.
Look for missing values in the dataset. You can use the report generated by ydata-profiling to identify missing values.
Look for correlations between different columns in the dataset. You can use the report generated by ydata-profiling to identify correlations between different columns.
Identify any outliers or unusual values in the dataset. You can use the report generated by ydata-profiling to identify any outliers or unusual values.
Summary
At the end of this exercise, write a summary of your findings. Did you find any interesting patterns or correlations in the data? Were there any issues or challenges you encountered while exploring the dataset? Use your summary to reflect on your experience using pandas and ydata-profiling to explore and understand a new dataset.

@author: iyino
"""

import pandas as pd
import sweetviz as sv
data = "C:/Users/iyino/OneDrive/Documents/data science/Creating-a-Calculator-Program/tutorials/Data-Science-Tutorial-Programs/Dataset/Tunisair_flights_dataset.csv"
dataset = pd.read_csv(data)

data_head = dataset.head(11)
print(data_head)
data_info = dataset.info()
print(data_info)
data_tail = dataset.tail(7)
missing = dataset.isnull().sum().sum()
data_describe = dataset.describe(include = "all")


myreport = sv.analyze(dataset)
myreport.show_html()


corr_1 = dataset.iloc[ :, 0 ].corr(dataset.iloc[:, 1])
corr_2 = dataset.iloc[:,1].corr(dataset.iloc[:,3])












