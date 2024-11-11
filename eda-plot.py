#Imports
import pandas as pd
import matplotlib.pyplot as plt

"""
Reads in a given CSV file, then filters rows based on the given time range. 

Parameters:
csv_file (str): The path to the CSV file.
start_time (int): The start time to filter the data.
end_time (int): The end time to filter the data.
"""
def read_csv(csv, start_time, end_time):
    #Load csv files 
    df = pd.read_csv(csv)

    #Drop unnecessary rows and columns 
    df.drop(index=0, inplace=True)
    df.drop(columns='events', inplace=True)

    #Convert all columns to numeric (if they aren't already)
    df = df.apply(pd.to_numeric, errors='coerce')

    #Filter rows based on the time range for the scanning period
    scan_df = df[(df['time'] >= start_time) & (df['time'] <= end_time)]

    return scan_df

"""
Takes the modified dataframe of the original CSV file and calculates statistical data. 
Returns a dataframe which composites all of the new data. 

Parameters: 
df (DataFrame (pandas)): The modified dataframe. 
"""
def calc_stat(df):
    #Make a copy of the dataframe for modification. 
    copy = df.copy()

    #Drop the time column when calculating statistics of the dataframe.
    copy.drop(columns='time', inplace=True)

    #Calculate the mean, median, and standard deviation
    avg_df = copy.mean(numeric_only=True)
    med_df = copy.median(numeric_only=True)
    sd_df = copy.std(numeric_only=True)

    #Combine the results into a DataFrame (renamed to pi_table)
    pi_table = pd.DataFrame({
        'Mean': avg_df,
        'Median': med_df,
        'Standard Deviation': sd_df
    })

    return pi_table

""" 


"""
def plot_all_groups(windows_group, blinds_group, hallway_group, category):
    fig, axes = plt.subplots(1, 3, figsize=(25, 5), sharey=True)
    fig.suptitle(f'{category} vs. Time for Different Groups\n', fontsize=24)

    # Pass the individual axes to each plot
    plot_trials(windows_group, category, 'Windows', ax=axes[0])
    plot_trials(blinds_group, category, 'Blinds', ax=axes[1])
    plot_trials(hallway_group, category, 'Hallway', ax=axes[2])

    return fig

""" 


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


"""
def plot_trials(total, category, group_name):     
    # Use ax to plot within the provided subplot axis
    plt.set_title(f'{group_name}:{category} vs. Time', fontsize=20)
    plt.set_xlabel('Time (s)', fontsize=15)
    plt.set_ylabel('Power (mW)', fontsize=15)
    plt.tick_params(axis='x', rotation=30, labelsize=15)

    min_time = 1000
    max_time = 0

    for i in range(len(total)):
        df = total[i].set_index('time')
        plot, = plt.plot(df.index, df[category])
        plot.set_label(f'Trial #{i+1}')

        min_time = min(min_time, df.index.min())
        max_time = max(max_time, df.index.max())
        
    plt.set_xlim(min_time, max_time)
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
    fig = plt.subplots(figsize=(16, 5))

    # Customize Plot
    plt.title(f'{category} vs. Time', fontsize=20)
    plt.xlabel('Time (s)', fontsize=15)
    plt.ylabel('Power (mW)', fontsize=15)
    plt.tick_params(axis='x', rotation=30, labelsize=15)

    df = df.set_index('time')
    plt.xlim(df.index.min(), df.index.max())

    plt.plot(df.index, df[category])
    plt.savefig(path, bbox_inches='tight')

    return fig

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
Takes the modified dataframe of the original CSV file and calculates statistical data. 
Returns a dataframe which composites all of the new data. 

Parameters: 
df (DataFrame (pandas)): The modified dataframe. 
"""
def print_to_file(df, output):
    #Format the text output for readability
    output_file = output
    with open(output_file, 'w') as file:
        #Write the header with spacing
        file.write(f"{'Metric':<25}{'Mean':<20}{'Median':<20}{'Standard Deviation':<20}\n")
        file.write("-" * 85 + "\n")  # Adjust separator line width
        
        for metric, row in df.iterrows():
            # Write only Mean, Median, and Standard Deviation
            file.write(f"{metric:<25}{row['Mean']:<20.2e}{row['Median']:<20.2e}{row['Standard Deviation']:<20.2e}\n")

    print(f"Data successfully saved to {output_file}")