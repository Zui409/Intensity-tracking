# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 13:53:02 2024
@author: zz409
"""

import pandas as pd
import numpy as np
import os 
import glob
import matplotlib.pyplot as plt
from scipy.signal import hilbert
from collections import defaultdict
import matplotlib.pyplot as plt

# Parameters to change
folder = r'D:\Folder'    # Data folder
Interval = 0.5            # Time interval between imaging frames   
min_track_length = 20     # Minimum number of positions on the track to be further considered


#Do not change
path_ROI = folder + r'\ROI.csv'
path_Int = folder + r'\Results.csv'
save_path = folder + r"\Plot"
if not os.path.exists(save_path): 
    os.makedirs(save_path)

#%% Function lib
def read_ROI_data(file_name):
    ROI_data = pd.read_csv(file_name, sep = ',', header = 0, engine='python')
    Index = ROI_data['Name'].copy()
    ID = Index.apply(lambda x: x.split("_")[1])
    time =ROI_data['Pos'].copy()
    ID_list = ID.tolist()
    time_point = time.tolist()
    
    return ID_list, time_point

def tidy_up_list(input_list):
    element_dict = defaultdict(list)
    index_dict = defaultdict(list)
    for index, element in enumerate(input_list):
        element_dict[element].append(element)
        index_dict[element].append(index)
    tidy_list = [element_dict[key] for key in sorted(element_dict.keys(), key=lambda x: input_list.index(x))]
    index_list = [index_dict[key] for key in sorted(index_dict.keys(), key=lambda x: input_list.index(x))]
    return tidy_list, index_list

def read_intensity_data(file_name):
    Int_data = pd.read_csv(file_name, sep = ',', header = 0, engine='python')
    Intensity = Int_data['Mean'].copy()
   
    return Intensity

def group_intensity(data_list, index_list):
    result = []
    for indices in index_list:
        group = [data_list[i] for i in indices]
        result.append(group)
    return result


def multiply_list(list_b, Interval):
    return [[element * Interval for element in sublist] for sublist in list_b]


def filter_lists_by_length(list_a, list_b,list_c, min_track_length):
    if len(list_a) != len(list_b):
        raise ValueError("The two lists must have the same length.")
    filtered_list_a = [sublist for sublist in list_a if len(sublist) >= min_track_length]
    filtered_list_b = [list_b[i] for i in range(len(list_b)) if len(list_a[i]) >= min_track_length]
    filtered_list_c = [list_c[i] for i in range(len(list_c)) if len(list_a[i]) >= min_track_length]
    return filtered_list_a, filtered_list_b,filtered_list_c

def save_track_info(track,path):
    df = pd.DataFrame({
        'Track name': [sublist[0] for sublist in track],
        'length': [len(sublist) for sublist in track]
    })

# Save the DataFrame to a CSV file
    directory_path = os.path.dirname(path_ROI)

    csv_file_path = directory_path+ r'\Track_info.csv'
    df.to_csv(csv_file_path, index=False)
    

def plot_lists(list_a, list_b,save_dir):
    # Flatten the lists and find min and max values
    flat_a = [item for sublist in list_a for item in sublist]
    flat_b = [item for sublist in list_b for item in sublist]

    min_x = min(flat_a)
    max_x = max(flat_a)
    min_y = min(flat_b)
    max_y = max(flat_b)

    if len(list_a) != len(list_b):
        raise ValueError("The two lists must have the same length.")

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for i, (sublist_a, sublist_b) in enumerate(zip(list_a, list_b)):
        plt.figure()  
        plt.plot(sublist_a, sublist_b)  
        plt.title(f'Cell {i+1}')
        plt.xlabel('Time (s)')
        plt.ylabel('Intensity (a.u.)')
        plt.xlim(min_x, max_x)
        plt.ylim(min_y, max_y)
        file_path = os.path.join(save_dir, f'Cell_{i+1}.png')
        plt.savefig(file_path)  
        plt.close()  
        data = {'Time': sublist_a, 'Intensity': sublist_b}
        df = pd.DataFrame(data)
        csv_file_path = os.path.join(save_dir, f'Cell_{i+1}.csv')
        df.to_csv(csv_file_path, index=False) 

# %% Code
Cell_id,time_point = read_ROI_data(path_ROI)
Int_data = read_intensity_data(path_Int)
tidy_list, index_list = tidy_up_list(Cell_id)
group_int = group_intensity(Int_data, index_list)
group_time = group_intensity(time_point, index_list)
group_track = group_intensity(Cell_id, index_list)
real_time = multiply_list(group_time, Interval)
fil_int, fil_time,fil_track= filter_lists_by_length(group_int,real_time,group_track,min_track_length)
plot_lists(fil_time, fil_int,save_path)
save_track_info(fil_track,path_ROI)