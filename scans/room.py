#Imports
import pandas as pd
import matplotlib.pyplot as plt

"""
This class creates an object that represents an environment type. It contains a list
which holds all the scans (dataframes) associated with the environment type. It also 
has attributes which can be references to determine which environment it is.

This also provides functions which allow for data visualization (time-series plots and 
boxplots). The functions can plot a single trial of a room or all trials of a room. 

Author(s): Allie Craddock, Casie Peng 

"""
###############

class Room:
    def __init__(self, room_type: str):
        """
        This is the constructor for the Room class object. It specifies the room type (the
        specific environment the scan took place in) and an internal list of trials (dataframe objects).

        Parameters:
        self (Room): the object itself
        room_type (str): the environment of the room type 
        """
        self.environment = room_type
        self.trials = []
    
    def add_trial(self, trial: pd.DataFrame):
        """
        This will add a dataframe (trial) to the internal trials list. 

        Parameter: 
        self (Room): the object itself
        trial (Dataframe (Pandas)): a dataframe representing another trial 
        """
        
        self.trials.add(trial)

    def plot_time_series(self, num: int, category: str):
        """
        Plots a time-series model of a singular dataframe for a certain performance indicator. 

        Parameters:
        self (Room): A Room object with a str identifier and a list of CSVs of a certain room type 
        num (int): The specific trial number of interest 
        category (str): The specific performance indicator of interest 
        """
        
        self.format_ts(self.environment, category)

        df = self.trials[num]
        df = df.set_index('time')
        plt.xlim(df.index.min(), df.index.max())

        plt.plot(df.index, df[category])

    def plot_time_series_trials(self, category: str):   
        """ 
        Plots a time-series model of all of the trials associated with an array of dataframes.
        This method does not require the axis parameter. 

        Parameters: 
        self (Room): A Room object with a str identifier and the list of CSVs of a certain room type 
        category (str): the performance indicator of interest
        """
    
        self.format_ts(self.environment, category)

        min_time = 1000
        max_time = 0

        for i in range(len(self.trials)):
            df = self.trials[i].set_index('time')
            fig, = plt.plot(df.index, df[category])
            fig.set_label(f'Trial #{i+1}')

            min_time = min(min_time, df.index.min())
            max_time = max(max_time, df.index.max())
            
        plt.xlim(min_time, max_time)
        plt.legend()

    def plot_box(self, num: int, category: str):
        """
        Plots a boxplot of a singular trial of a single room type. 

        Parameters: 
        self (Room): A Room object with a str identifier and a list of CSVs of a certain room type 
        num (int): The specific trial number of interest 
        category (str): The performance indicator of interest
        """
        
        df = self.trials[num]
        data = df[category].to_numpy()
        self.format_bp(self.environment, category)
        plt.boxplot(data)

    def plot_box_trials(self, category: str):
        """
        Plots a boxplot of all trials of a singular room type. 

        Parameters:
        self (Room): A Room object with a str identifier and a list of CSVs of a certain room type 
        category (str): The performance indicator of interest
        """
        
        self.format_bp(self.environment, category)

        for i in range(len(self.trials)):
            data = [self.trials[i][category].to_numpy()]
            plt.boxplot(data, positions=[i + 1], labels=[f'Trial #{i+1}'], widths=0.4)

    @staticmethod
    def format_ts(room_type: str, category: str):
        """ 
        Formats time-series plots. Adjusts size of the plots and font sizes. Adds a title and axes labels. 

        Parameters: 
        room_type (str): the room type of the data
        category (str): the performance indicator of interest 
        """
    
        plt.figure(figsize=(16, 5))
        plt.title(f'{room_type}: {category} vs. Time', fontsize=20)
        plt.xlabel('Time (s)', fontsize=15)
        plt.ylabel('Power (mW)', fontsize=15)
        plt.tick_params(axis='x', rotation=30, labelsize=15)

    @staticmethod
    def format_bp(room_type: str, category: str):
        """
        Formats boxplots. Adjusts the size of the plots and font sizes. Adds a title and axes labels. 

        Parameters: 
        room_type (str): the room type of the data
        category (str): the performance indicator of interest 
        """
        
        plt.figure(figsize=(10, 5))
        plt.title(f'{room_type}: {category}', fontsize=20)
        plt.xlabel(f'{room_type} Scans', fontsize=15)
        plt.ylabel('Power (mW)', fontsize=15)