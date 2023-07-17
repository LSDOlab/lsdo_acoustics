import numpy as np
import pickle
from pathlib import Path

# FILE NAME
from pathlib import Path
root_path = Path(__file__).parents[0]
file_title = 'idealtwist_out'
file_name = file_title + '.csv'
file_path = root_path / 'data_files' / file_name

import csv
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

len_rows = len(rows[1:])
data = rows[1:]

non_dim_rad = []
lambda_i = []
AoA = []
dCTdr = []
Cl = []
Cd = []


for i in range(len_rows):
    non_dim_rad.append(float(data[i][0]))
    lambda_i.append(float(data[i][1]))
    AoA.append(float(data[i][2]))
    dCTdr.append(float(data[i][3]))
    Cl.append(float(data[i][4]))
    Cd.append(float(data[i][5]))

data_dict = {
    'non_dim_rad': non_dim_rad,
    'lambda_i': lambda_i,
    'AoA': AoA,
    'dCTdr': dCTdr,
    'Cl': Cl,
    'Cd': Cd
}

# SAVING DATA
import pickle
file = open('data_files/' + file_title + '.pkl','wb')
pickle.dump(data_dict, file)
file.close