import numpy as np
import os

# FILE NAME
from pathlib import Path
root_path = Path(__file__).parents[0]
file_title = 'loading_Jamaluddin'
file_name = file_title + '.csv'
file_path = root_path / 'data_files' / file_name

# DATA EXTRACTION
import csv
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

len_rows = len(rows[2:])
init_row = 2
rows_per_rotor = 40

rows_per_timestep = 84
time = []
data_r1 = []
angle_r1 = []

data_r2 = []
angle_r2 = []

dataset = 0
while True:
    try:
        init_row += rows_per_timestep
        time_t = float(rows[init_row+2][2])
        time.append(time_t)
    
        initial_row_r1 = init_row # THIS ROW IS THE PARAMETERS t, x, y, ...
        data_r1_t = []
        angle_r1_t = float(rows[init_row+2][1])
        angle_r1.append(angle_r1_t)
        print('r1')
        for i in range(40):
            print(init_row+3+i, rows[init_row+3+i])
            data_r1_t.append(
                [float(val) for val in rows[init_row+3+i][1:8]]
            )
        
        data_r1.append(data_r1_t)
    
        initial_row_r2 = init_row + 3 + 41
        data_r2_t = []
        angle_r2_t = float(rows[init_row+2+41][1])
        print('r2')
        angle_r2.append(angle_r2_t)
        for i in range(40):
            print(init_row+3+41+i, rows[init_row+3+41+i])
            data_r2_t.append(
                [float(val) for val in rows[init_row+3+41+i][1:8]]
            )
        
        data_r2.append(data_r2_t)
    
        dataset += 1
    except:
        break

# DATA PARSING
'''
Need data to be of shape (num_radial, num_tangential)
- num_tangential is equal to the number of time steps
- num_radial is equal to rows_per_rotor

OUTPUTS:
    - sectional Z-force (in the drag direction)
    - sectional X-force (in the thrust direction)
    - chord distribution
'''

num_tan = len(time)
num_radial = rows_per_rotor

# CHORD DISTRIBUTION
c = np.zeros((num_radial,))
for i in range(num_radial):
    c[i] = data_r1[0][i][1] # Extracting from just first time step

# TIME AND ANGLE
time = np.array(time)
angle = np.array(angle_r1)

# FORCES
fz = np.zeros((num_radial, num_tan))
fx = np.zeros((num_radial, num_tan))

for i in range(num_tan):
    for j in range(num_radial):
        fz[j,i] = data_r1[i][j][6]
        fx[j,i] = data_r1[i][j][0]

data_dict = {'fx': fx, 'fz': fz, 'c': c, 'time': time, 'angle': angle}

# SAVING DATA
import pickle
file = open(file_title,'wb')
pickle.dump(data_dict, file)
file.close