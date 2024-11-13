#Imports
import matplotlib.pyplot as plt

"""
This class focuses on using cleaned datasets for visual analysis. Functions provided can plot the time series data 
of a performance indicator of room types for a single trial of a single room type, all trials of one room type, 
and all trials for all room types. Other data analysis measures TBA. 

Author(s):

"""
###############


""" 
This function plots the windows, blinds, and hallway trials on subplots for a performance indicator ('category'). 

windows_group (arr[Dataframe (Pandas)]): All of the CSV files correlated to the windows group. 
blinds_group (arr[Dataframe (Pandas)]): All of the CSV files correlated to the blinds group. 
hallway_group (arr[Dataframe (Pandas)]): All of the CSV files correlated to the hallway group. 
category (str): The performance indicator of interest. 

"""
def plot_all_groups(windows_group, blinds_group, hallway_group, category):
    fig, axes = plt.subplots(1, 3, figsize=(25, 5), constrained_layout=True)
    fig.suptitle(f'{category} vs. Time for Different Groups\n', fontsize=24)

    # Pass the individual axes to each plot
    plot_trials(windows_group, category, 'Windows', ax=axes[0])
    plot_trials(blinds_group, category, 'Blinds', ax=axes[1])
    plot_trials(hallway_group, category, 'Hallway', ax=axes[2])

""" 
Plots all of the trials associated with an array of dataframes. 
Helper method for the plot_all_groups method, which accepts an additional axis parameter. 

total (arr[Dataframe (Pandas)]): the array of CSVs of a certain room type 
category (str): the performance indicator of interest
group_name (str): the name of the room type 
ax (axes): which axes the CSVs are plotted to from a group of subplots

"""
def plot_trials(total, category, group_name, ax):     
    # Use ax to plot within the provided subplot axis
    ax.set_title(f'{group_name}:{category} vs. Time', fontsize=20)
    ax.set_xlabel('Time (s)', fontsize=15)
    ax.set_ylabel('Power (mW)', fontsize=15)
    ax.tick_params(axis='x', rotation=30, labelsize=15)

    min_time = 1000
    max_time = 0

    for i in range(len(total)):
        df = total[i].set_index('time')
        plot, = ax.plot(df.index, df[category])
        plot.set_label(f'Trial #{i+1}')

        min_time = min(min_time, df.index.min())
        max_time = max(max_time, df.index.max())
        
    ax.set_xlim(min_time, max_time)
    ax.legend()

""" 
Plots all of the trials associated with an array of dataframes. This method does not require the axis parameter. 

total (arr[Dataframe (Pandas)]): the array of CSVs of a certain room type 
category (str): the performance indicator of interest
group_name (str): the name of the room type 
"""
def plot_all_trials(total, category, group_name):   
    plt.figure(figsize=(16, 5))
    plt.title(f'{group_name}:{category} vs. Time', fontsize=20)
    plt.xlabel('Time (s)', fontsize=15)
    plt.ylabel('Power (mW)', fontsize=15)
    plt.tick_params(axis='x', rotation=30, labelsize=15)

    min_time = 1000
    max_time = 0

    for i in range(len(total)):
        df = total[i].set_index('time')
        plot, = plt.plot(df.index, df[category])
        plot.set_label(f'Trial #{i+1}')

        min_time = min(min_time, df.index.min())
        max_time = max(max_time, df.index.max())
        
    plt.xlim(min_time, max_time)
    plt.legend()

"""
This will plot a singular dataframe for a certain performance indicator, then saves the plot to a particular path. 

Parameters:
df (Dataframe (pandas)): the specific dataframe to be plotted
category (str): the specific performance indicator interested
path (str): the path which the file will be saved to

Returns a plot of a single trial. 

"""
def plot_csv(df, category, path):
    plt.subplots(figsize=(16, 5))

    # Customize Plot
    plt.title(f'{category} vs. Time', fontsize=20)
    plt.xlabel('Time (s)', fontsize=15)
    plt.ylabel('Power (mW)', fontsize=15)
    plt.tick_params(axis='x', rotation=30, labelsize=15)

    df = df.set_index('time')
    plt.xlim(df.index.min(), df.index.max())

    plt.plot(df.index, df[category])
    plt.savefig(path, bbox_inches='tight')

"""
Saves and displays the given figure.

Parameters:
fig (matplotlib.figure.Figure): The figure to save and display.
path (str): The path to save the figure to.
"""
def save(path):
    plt.savefig(path, bbox_inches='tight')  # Save the figure
    plt.show()  # Display the figure