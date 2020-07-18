## using pandas library

import pandas as pd

# @sep: can be space, tab, comma, etc.
read_file = pd.read_csv ('textfile.txt', sep=' ')

# @index: whether or not to have an index column
read_file.to_csv('outputcsv.csv', index=None)
