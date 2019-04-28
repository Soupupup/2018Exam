import numpy as np
import csv
import json
from matplotlib import pyplot as plt
# import csv file
rain_csvFile = 'python_language_1_data.csv'
rain_jsonFile = 'rainfall.json'


# question a.)
# extract and convert daily rainfall depth
# into a dictionary
def read_csv(filename):
    # create dictionary
    dict = {}
    with open(filename) as rainFile:
        csvReader = csv.reader(rainFile)
        # ignores header
        next(csvReader, None)
        for row in csvReader:
            # create new dict key as each year if it doesn't exist
            # dict value=list of daily rainfall of given year
            dict.setdefault(int(row[0]), []).append(float(row[2]))

    return dict

# create rainfall dictionary
rainfall_dict = read_csv(rain_csvFile)
# converts rainfall dictionary to json format
with open(rain_jsonFile, 'w') as outfile:
    json.dump(rainfall_dict, outfile, indent=4)


# question b.)
# extract rainfall dictionary
def load_json_content(filename):
    with open(filename, 'r') as file:
        content = json.loads(file.read())
    return content


# extracts and plot daily rain for a given year
def plot_dailyRain(jsonfile, year, line_color='lightblue'):
    # extract rainfall dictionary from json
    rain_dict = load_json_content(jsonfile)
    #extract rainfall of given year
    rain_depth = rain_dict[str(year)]
    # plot time series and saves figure
    fig = plt.figure()
    ax = fig.add_subplot(111)
    day = np.arange(1, len(rain_depth) + 1)
    ax.plot(day, rain_depth, color=line_color)
    plt.ylabel('Daily Rainfall (mm)')
    plt.xlabel('Day')
    plt.title('Rainfall per day over a year')
    plt.savefig(str(year) + '.png')


plot_dailyRain(rain_jsonFile, 1998)


# question c.)
#plots mean annual rainfall for a given time period
def plot_mean_annualRain(jsonfile, start, end, line_color='lightblue'):
    # extract rainfall dictionary from json
    rain_dict = load_json_content(jsonfile)
    # list of years within time-period
    period = np.arange(start, end + 1)
    # empty list size of nbr mean values
    period_rain = np.empty((len(period,)))
    # calculates mean rainfall or each year
    for nbr, year in enumerate(period):
        rain_list = rain_dict[str(year)]
        rain_mean = np.sum(rain_list) / len(rain_list)
        # appends mean value to list
        period_rain[nbr] = rain_mean
    # plots and saves mean rainfall
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(period, period_rain, color=line_color)
    plt.ylabel('Mean Daily Rainfall (mm)')
    plt.xlabel('Year')
    plt.title('Mean annual rainfall across a timeperiod')
    plt.savefig(str(start) + 'to' + str(end) + '.png')


plot_mean_annualRain(rain_jsonFile, 1988, 2000)


# question d.)
# corrects a given value
def correction(value):
    updated_value = np.power(value * 1.2, np.sqrt(2))

    return updated_value


# fucntion 1
def correction_forloop(jsonfile, year):
    """
    For-loop:
    + easy to understand
    - more lines of code
    -slower computationally

    comprehension list:
    + shorter/simpler code
    + faster computationally
    - harder to understand
    """
    rain = load_json_content(jsonfile)
    daily_rain = rain[str(year)]
    for index, depth in enumerate(daily_rain):
        daily_rain[index] = correction(daily_rain[index])

    return daily_rain


# function 2
def correction_list(jsonfile, year):
    rain = load_json_content(jsonfile)
    rain_list = rain[str(year)]
    daily_rain = [correction(value) for value in rain_list]

    return daily_rain

forloop = correction_forloop(rain_jsonFile, 2005)
list_comp = correction_list(rain_jsonFile, 2005)
