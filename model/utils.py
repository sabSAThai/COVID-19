import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import params


def plot_confirmed_cases(country, confirmed_cases_df, start, end, log_flag=False):

	column_header = confirmed_cases_df.columns.values

	confirmed_cases = confirmed_cases_df.loc[confirmed_cases_df[column_header[1]] == country]
	
	num_days = end - start
	days = np.linspace(start, end, num=num_days)
	
	confirmed_cases = np.ravel(confirmed_cases.values)
	confirmed_cases = confirmed_cases[4:]
	confirmed_cases = confirmed_cases[start:end]
	
	if log_flag:
		confirmed_cases = confirmed_cases.astype(float)
		confirmed_cases = np.log(confirmed_cases)

	plt.plot(days, confirmed_cases)
	plt.title(country)
	plt.ylabel('Confirmed cases')
	plt.xlabel('Day')

