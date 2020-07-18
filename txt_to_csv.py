import pandas as pd

read_file = pd.read_csv ('textfile.txt', sep=' ')
read_file.to_csv('outputcsv.csv', index=None)
