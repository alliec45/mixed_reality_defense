#Imports
import pandas as pd

"""
These functions use Exploratory Data Analysis Techniques (EDA). It focuses on using Dataframes for an input of CSV files. Then it cleans and isolates 
parts of the data which we're interested in. It also calculates information such as mean, median, and standard deviation of the performance 
indicators of each CSV file. It can print this information to a file. 

Author(s): Allie Craddock, Casie Peng 

"""
###############

def csv_to_df(csv: str, start_time: int, end_time: int, window_slide: bool):
    """
    Reads in a given CSV file, filters rows based on the given time range, 
    and computes the mean of performance indicators for each second if window
    sliding technique is confirmed. 

    Parameters:
    csv_file (str): The path to the CSV file.
    start_time (int): The start time to filter the data.
    end_time (int): The end time to filter the data.
    window_slide (bool): Applies window_sliding technique if true. 

    Returns:
    pd.DataFrame: A dataframe of the cleaned CSV. 
    """
    
    # Load csv file
    df = pd.read_csv(csv)

    # Drop unnecessary rows and columns
    df.drop(index=0, inplace=True)
    df.drop(columns='events', inplace=True)

    # Convert all columns to numeric (if they aren't already)
    df = df.apply(pd.to_numeric, errors='coerce')

    # Filter rows based on the time range for the scanning period
    filtered_df = df[(df['time'] >= start_time) & (df['time'] <= end_time)].copy()

    if (window_slide):
        # Group by integer part of 'time' (grouping by second)
        filtered_df['second'] = filtered_df['time'].astype(int)
        grouped_df = filtered_df.groupby('second').mean()

        # Add a 'time' column for time-series plotting (set to the start of the second)
        grouped_df['time'] = grouped_df.index

        # Reset index to make 'time' and 'second' columns instead of indices
        grouped_df.reset_index(drop=True, inplace=True)
        return grouped_df

    return filtered_df

def calc_stat(df: pd.DataFrame):
    """
    Takes the modified dataframe of the original CSV file and calculates statistical data. 
    Returns a dataframe which composites all of the new data. 

    Parameters: 
    df (DataFrame (pandas)): The modified dataframe. 
    """
    
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

def calc_comb_stat(all_df: list):
    """
    Takes a group of modified dataframes, combines them into one, 
    and uses calc_stat(df) above to calculate statistics. 

    Parameters:
    all_df (list[Dataframe (pandas)]): all of the dataframes to be combined 
    """
    combined = pd.concat(all_df, ignore_index=True)
    return calc_stat(combined)

def print_to_file(df: pd.DataFrame, output: str):
    """
    Takes the modified dataframe of the original CSV file and calculates statistical data. 
    Returns a dataframe which composites all of the new data. 

    Parameters: 
    df (DataFrame (pandas)): The modified dataframe. 
    output (str): Path to the output file. 
    """
    
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