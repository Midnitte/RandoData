import pandas as pd
import numpy as np
import random
import sys
import pathlib
import string
from datetime import datetime

# TODO:
# Ensure generated company names are unique
# OverflowError: int too large to convert to float

test_data = pd.DataFrame()

def string_generator(size):
    chars = string.ascii_uppercase + string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(size))

def word_generator(num, max_size=10):
    """Return a string of random length (1-10) num times"""
    words = []
    for num in range(num):
        r_number = random.randint(1,max_size)
        words.append(string_generator(r_number))
    return words


def save_file(file_name, file_type='xlsx'):
    """Save xlsx file as file_name"""
    if file_type is 'xlsx':
        save_name = (sys.path[0] + '\\'+ file_name + '.xlsx')
        save_name_path = pathlib.Path(save_name)
        if save_name_path.is_file():
            print('File already exists.')
        else:
            test_data.to_excel(save_name)
    elif file_type is 'csv':
        save_name = (sys.path[0] + '\\'+ file_name + '.csv')
        save_name_path = pathlib.Path(save_name)
        if save_name_path.is_file():
            print('File already exists.')
        else:
            test_data.to_csv(save_name)
    else:
        print('File not saved. Invalid filetype.')

def linear_graph(size, positive=True):
    """Take a size and return either a positive or negative linear set, adjusted by a random number"""
    graph_frame = []
    if positive:
        for i in range(size):
            graph_frame.append(i + 1 + np.round(np.random.uniform(low=0.5, high=5), decimals=2))
    else:
        for i in range(size):
            graph_frame.append(i - 1 - np.round(np.random.uniform(low=0.5, high=5), decimals=2))
    return graph_frame

def exponential_graph(size, positive=True):
    """Take a size and return either a positive or negative exponential set, adjusted by a random number"""
    graph_frame = []
    if positive:
        for i in range(size):
            graph_frame.append(i*i + np.round(np.random.uniform(low=0.5, high=5), decimals=2))
    else:
        for i in range(size):
            graph_frame.append(-i*i - np.round(np.random.uniform(low=0.5, high=5), decimals=2))
    return graph_frame

def cubic_graph(size, positive=True):
    """Take a size and return either a positive or negative cubic set, adjusted by a random number"""
    graph_frame = []
    if positive:
        for i in range(size):
            graph_frame.append(i*i*i + np.round(np.random.uniform(low=0.5, high=5), decimals=2))
    else:
        for i in range(size):
            graph_frame.append(-i*i*i - np.round(np.random.uniform(low=0.5, high=5), decimals=2))
    return graph_frame

def expo_graph(size, positive=True):
    """Take a size and return either a positive or negative expo set, adjusted by a random number"""
    graph_frame = []
    if positive:
        for i in range(size):
            graph_frame.append(5**i + np.round(np.random.uniform(low=0.0, high=0.5), decimals=2))
    else:
        for i in range(size):
            graph_frame.append(5**(-i) - np.round(np.random.uniform(low=0.0, high=0.5), decimals=2))
    return graph_frame


def random_dates(n, unit='D', seed=None):
    """Return random dates between a year n times"""
    start_time = pd.to_datetime('2019-01-01', infer_datetime_format=True )
    end_time = pd.to_datetime('2019-12-31', infer_datetime_format=True )
    time_frame = []
    if not seed:
        np.random.seed(0)

    ndays = (end_time - start_time).days + 1
    time_frame.append(start_time + pd.to_timedelta(
        np.random.randint(0, ndays, n), unit=unit
    ))
    returned_time = pd.DataFrame(time_frame).transpose()
    returned_time.columns = ['Dates']
    ordered_time = returned_time.sort_values('Dates').reset_index(drop=True)
    return ordered_time

list_of_graphs = [cubic_graph, exponential_graph, linear_graph, expo_graph]

list_of_companies = word_generator(500)

def build_dataframe():
    """Return a dataframe made of several companies with random data"""
    my_frame_data = pd.DataFrame()
    for company in list_of_companies:
        mini_data = pd.DataFrame()
        mini_data['Data'] = random.choice(list_of_graphs)(200)
        mini_data['Company'] = company
        mini_data['Dates'] = random_dates(200)
        my_frame_data = my_frame_data.append(mini_data, ignore_index=True) # Append doesn't happen in-place, so we have to store it..
    my_frame_data = my_frame_data[['Dates', 'Company', 'Data']] # Reorder the columns
    return my_frame_data



example = build_dataframe()

build_dataframe().to_csv('savederp3.csv')

print(example)



