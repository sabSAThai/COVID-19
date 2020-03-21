import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import params
import utils


data_dir = params.data_dir
filepath = data_dir + 'time_series_19-covid-Confirmed.csv'

confirmed_cases = pd.read_csv(filepath)
column_header = confirmed_cases.columns.values

initial_date = '1/22/20'
final_date = '3/19/20'
date_array = column_header[4:]

start, end = (20, 40)

utils.plot_confirmed_cases('Italy', confirmed_cases, start, end, log_flag=False)
plt.figure()
utils.plot_confirmed_cases('Italy', confirmed_cases, start, end, log_flag=True)

utils.plot_confirmed_cases('India', confirmed_cases, 20, len(date_array),log_flag=False)
plt.figure()
utils.plot_confirmed_cases('India', confirmed_cases, 20, len(date_array),log_flag=True)

utils.plot_confirmed_cases('Japan', confirmed_cases, 0, len(date_array),log_flag=False)
plt.figure()
utils.plot_confirmed_cases('Japan', confirmed_cases, 0, len(date_array),log_flag=True)


import pdb; pdb.set_trace()
