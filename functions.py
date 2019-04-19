import pandas as pd
import pickle


# pickle writer
def pickle_write(data, filename, byte=True):
    print('-' * 80)
    print('Writing...')
    if byte:
        with open(filename, 'wb') as fw:
            pickle.dump(data, fw)
        print('Writing has finised.')
    else:
        with open(filename, 'w') as fw:
            pickle.dump(data, fw)
        print('Writing has finised.')


# pickle reader
def pickle_read(filename, byte=True):
    print('-' * 80)
    print('Loading...')
    if byte:
        with open(filename, 'rb') as fw:
            data = pickle.load(fw)
        print('Loading has finised.')
        return data
    else:
        with open(filename, 'r') as fw:
            data = pickle.load(fw)
        print('Loading has finised.')
        return data
