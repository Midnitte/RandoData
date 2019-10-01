import pandas as pd
import numpy as np
import random
import sys
import pathlib
import string

def random_dates2(start, end, n, unit='D', seed=None):
    if not seed:  # from piR's answer
        np.random.seed(0)

    ndays = (end - start).days + 1
    return start + pd.to_timedelta(
        np.random.randint(0, ndays, n), unit=unit
    )



test_data = pd.DataFrame()



def string_generator(size):
    chars = string.ascii_uppercase + string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(size))

def word_generator(num):
    """Return a string of random length (1-10) n times"""
    words = []
    for num in range(num):
        r_number = random.randint(1,10)
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
    else:
        save_name = (sys.path[0] + '\\'+ file_name + '.csv')
        save_name_path = pathlib.Path(save_name)
        if save_name_path.is_file():
            print('File already exists.')
        else:
            test_data.to_csv(save_name)


def generate_data(gfile_name, gfile_type='xlsx', data_size=6):
    start_time = pd.to_datetime('2018-01-01')
    end_time = pd.to_datetime('2018-12-31')
    random_dates = random_dates2(start_time, end_time, data_size)
    global test_data
    test_data['Dates'] = random_dates

    test_data['Companies'] = word_generator(data_size)
    random_numbers = pd.DataFrame(np.random.randint(0,100,size=(data_size, 4)), columns=list('ABCD'))
    test_data = pd.concat([test_data, random_numbers], axis=1)
    random_floats = pd.DataFrame(np.round(np.random.uniform(low=0.5, high=13.3, size=(data_size, 4)), decimals=2), columns=list('EFGH'))
    test_data = pd.concat([test_data, random_floats], axis=1)

    save_file(gfile_name, file_type=gfile_type)

generate_data('derpd', gfile_type='csv', data_size=6000)
print(test_data)
