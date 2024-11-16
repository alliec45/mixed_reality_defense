#Imports
import matplotlib.pyplot as plt
import numpy as np

"""
This class focuses on using cleaned datasets for visual analysis. Functions provided can plot the time series data 
of a performance indicator of room types for a single trial of a single room type, all trials of one room type, 
and all trials for all room types. Other data analysis measures TBA. 

Author(s): Allie Craddock, Casie Peng 

"""
###############

"""
Plots a time-series model of a singular dataframe for a certain performance indicator. 

Parameters:
df (Dataframe (pandas)): the specific dataframe to be plotted
category (str): the specific performance indicator interested

"""
def plot_time_series(df, category):
    room_type = df.name
    format_ts(room_type, category)

    df = df.set_index('time')
    plt.xlim(df.index.min(), df.index.max())

    plt.plot(df.index, df[category])

""" 
Plots a time-series model of all of the trials associated with an array of dataframes.
This method does not require the axis parameter. 

Parameters: 
total (arr[Dataframe (Pandas)]): the array of CSVs of a certain room type 
category (str): the performance indicator of interest

"""
def plot_time_series_trials(total, category):   
    room_type = total[0].name 
    format_ts(room_type, category)

    min_time = 1000
    max_time = 0

    for i in range(len(total)):
        df = total[i].set_index('time')
        fig, = plt.plot(df.index, df[category])
        fig.set_label(f'Trial #{i+1}')

        min_time = min(min_time, df.index.min())
        max_time = max(max_time, df.index.max())
        
    plt.xlim(min_time, max_time)
    plt.legend()

""" 
This function plots a time-series model of the trials of all room types on subplots 
for a performance indicator ('category'). 

Parameters: 
total (arr[Dataframe (Pandas)]): All of arrays of CSV files correlated by room type. 
category (str): The performance indicator of interest. 

"""
def plot_time_series_all(total, category):
    size = len(total)
    fig, axes = plt.subplots(1, size, figsize=(25, 5), constrained_layout=True)
    fig.suptitle(f'{category} vs. Time for Different Groups\n', fontsize=24)

    # Pass the individual axes to each plot
    for i in range(size):
        get_time_series_trials(total[i], category, ax=axes[i])

        axes[i].set_title(total[i][0].name, fontsize=20)
        axes[i].set_xlabel('Time (s)', fontsize=15)
        axes[i].set_ylabel('Power (mW)', fontsize=15)


""" 
Plots a time-series model of all of the trials associated with an array of dataframes. 
Helper method for the plot_all_groups method, which accepts an additional axis parameter. 

Parameters: 
total (arr[Dataframe (Pandas)]): the array of CSVs of a certain room type 
category (str): the performance indicator of interest
group_name (str): the name of the room type 
ax (axes): which axes the CSVs are plotted to from a group of subplots

"""
def get_time_series_trials(total, category, ax):     
    min_time = 1000
    max_time = 0

    for i in range(len(total)):
        df = total[i].set_index('time')
        fig, = ax.plot(df.index, df[category])
        fig.set_label(f'Trial #{i+1}')

        min_time = min(min_time, df.index.min())
        max_time = max(max_time, df.index.max())
        
    ax.set_xlim(min_time, max_time)
    ax.legend()

"""
Plots a boxplot of a singular trial of a single room type. 

Parameters: 
df (Dataframe (pandas)): The dataframe that is plotted
category (str): The performance indicator of interest
"""
def plot_box(df, category):
    data = df[category].to_numpy()
    format_bp(df.name, category)
    plt.boxplot(data)

"""
Plots a boxplot of all trials of a singular room type. 

Parameters:
total (arr[Dataframe (pandas)]): The dataframes that are plotted
category (str): The performance indicator of interest

"""
def plot_box_trials(total, category):
    room_type = total[0].name 
    format_bp(room_type, category)

    for i in range(len(total)):
        data = [total[i][category].to_numpy()]
        plt.boxplot(data, positions=[i + 1], labels=[f'Trial #{i+1}'], widths=0.4)

"""
Plot a boxplot for all trials of all room types. 

Parameters:
total (arr[Dataframe (pandas)]): The array of arrays of dataframes that are plotted
category (str): The performance indicator of interest

"""
def plot_box_all(total, category):
    size = len(total)
    fig = plt.figure(figsize=(10, 7), constrained_layout=True)
    ax = fig.add_subplot(1, 1, 1)

    ax.set_title(f'{category} for Different Groups\n', fontsize=24)
    total_trials = 0

    # Pass the individual axes to each plot
    for i in range(size):
        get_box_trials(total[i], category, total_trials, ax)
        total_trials += len(total[i])

    ax.set_ylabel('Power (mW)', fontsize=15)
    ax.tick_params(axis='x', rotation=90)
    

"""
Plots a boxplot of all trials of a singular room type. Takes in an extra figure parameter.

Parameters:
total (arr[Dataframe (pandas)]): The array of dataframes that are plotted
category (str): The performance indicator of interest
size (int): The number of groups (room types) that are plotted
ax (axes): The subplot which will be plotted on 

"""
def get_box_trials(total, category, size, ax):
    for i in range(len(total)):
        data = [total[i][category].to_numpy()]
        room_type = total[i].name
        ax.boxplot(data, positions=[(size) + i], labels=[f'{room_type}: Trial #{(i + 1)}'], widths=0.6)

"""
Saves and displays the given figure.

Parameters:
fig (matplotlib.figure.Figure): The figure to save and display.
path (str): The path to save the figure to.

"""
def save(path):
    plt.savefig(path, bbox_inches='tight')  # Save the figure
    plt.show()  # Display the figure

""" 
Formats time-series plots. Adjusts size of the plots and font sizes. Adds a title and axes labels. 

Parameters: 
room_type (str): the room type of the data
category (str): the performance indicator of interest 

"""
def format_ts(room_type, category):
    plt.figure(figsize=(16, 5))
    plt.title(f'{room_type}: {category} vs. Time', fontsize=20)
    plt.xlabel('Time (s)', fontsize=15)
    plt.ylabel('Power (mW)', fontsize=15)
    plt.tick_params(axis='x', rotation=30, labelsize=15)

"""
Formats boxplots. Adjusts the size of the plots and font sizes. Adds a title and axes labels. 

Parameters: 
room_type (str): the room type of the data
category (str): the performance indicator of interest 

"""
def format_bp(room_type, category):
    plt.figure(figsize=(10, 5))
    plt.title(f'{room_type}: {category}', fontsize=20)
    plt.xlabel(f'{room_type} Scans', fontsize=15)
    plt.ylabel('Power (mW)', fontsize=15)