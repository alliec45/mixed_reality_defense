#Imports
import matplotlib.pyplot as plt
import numpy as np
from room import Room

"""
These functions use cleaned datasets for visual analysis. Functions provided can plot the time series data 
of a performance indicator of room types for a single trial of a single room type, all trials of one room type, 
and all trials for all room types. Other data analysis measures TBA. 

Author(s): Allie Craddock, Casie Peng 

"""
###############

""" 
This function plots a time-series model of the trials of all room types on subplots 
for a performance indicator ('category'). 

Parameters: 
total_rooms (list): The list of Room objects 
category (str): The performance indicator of interest. 

"""
def plot_time_series_all(total_rooms: list, category: str):
    size = len(total_rooms)

    if (size == 0):
        print("This list is empty")
    else: 
        fig, axes = plt.subplots(1, size, figsize=(25, 5), constrained_layout=True)
        fig.suptitle(f'{category} vs. Time for Different Groups\n', fontsize=24)

        # Pass the individual axes to each plot
        for i in range(size):
            get_time_series_trials(total_rooms[i], category, ax=axes[i])

            axes[i].set_title((total_rooms[i]).environment, fontsize=20)
            axes[i].set_xlabel('Time (s)', fontsize=15)
            axes[i].set_ylabel('Power (mW)', fontsize=15)

"""
Loops through and plots every performance indicator (pi) in a time series (ts) model 
for all trials for all room types on different subplots. 

Parameters:
total_rooms (list): A list of Room objects

"""
def ts_pi(total_rooms: list):
    size = len(total_rooms)

    if (size == 0):
        print("This list is empty")
    else:
        column_names = list(total_rooms[0].trials[0].columns.values)
        if "time" in column_names:
            column_names.remove("time")

        for col in column_names:
            plot_time_series_all(total_rooms, col)
            save(f'data_analysis/plots/all_{col}')

""" 
Plots a time-series model of all of the trials associated with an array of dataframes. 
Helper method for the plot_all_groups method, which accepts an additional axis parameter. 

Parameters: 
room (Room): A Room object with a str identifier and the list of CSVs of a certain room type 
category (str): the performance indicator of interest
ax (axes): which axes the CSVs are plotted to from a group of subplots

"""
def get_time_series_trials(room: Room, category: str, ax: plt.axes):     
    min_time = 1000
    max_time = 0

    for i in range(len(room.trials)):
        df = room.trials[i].set_index('time')
        fig, = ax.plot(df.index, df[category])
        fig.set_label(f'Trial #{i+1}')

        min_time = min(min_time, df.index.min())
        max_time = max(max_time, df.index.max())
        
    ax.set_xlim(min_time, max_time)
    ax.legend()

"""
Plot a boxplot for all trials of all room types. 

Parameters:
total_rooms (list): The list of Room objects 
category (str): The performance indicator of interest

"""
def plot_box_all(total_rooms: list, category: str):
    size = len(total_rooms)
    fig = plt.figure(figsize=(10, 7), constrained_layout=True)
    ax = fig.add_subplot(1, 1, 1)

    ax.set_title(f'{category} for Different Groups\n', fontsize=24)
    total_trials = 0

    # Pass the individual axes to each plot
    for i in range(size):
        get_box_trials(total_rooms[i], category, total_trials, ax)
        total_trials += len(total_rooms[i].trials)

    ax.set_ylabel('Power (mW)', fontsize=15)
    ax.tick_params(axis='x', rotation=90)
    

"""
Plots a boxplot of all trials of a singular room type. Takes in an extra figure parameter.

Parameters:
room (Room): A Room object with a str identifier and a list of CSVs of a certain room type 
category (str): The performance indicator of interest
size (int): The number of groups (room types) that are plotted
ax (axes): The subplot which will be plotted on 

"""
def get_box_trials(room: Room, category: str, size: int, ax: plt.axes):
    for i in range(len(room.trials)):
        data = [room.trials[i][category].to_numpy()]
        ax.boxplot(data, positions=[(size) + i], labels=[f'{room.environment}: Trial #{(i + 1)}'], widths=0.6)

"""
Saves and displays the given figure.

Parameters:
fig (matplotlib.figure.Figure): The figure to save and display.
path (str): The path to save the figure to.

"""
def save(path: str):
    plt.savefig(path, bbox_inches='tight')  # Save the figure
    plt.show()  # Display the figure