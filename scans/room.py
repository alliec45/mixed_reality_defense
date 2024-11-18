#Imports


"""
This class creates an object that represents an environment type. It contains a list
which holds all the scans (dataframes) associated with the environment type. It also 
has attributes which can be references to determine which environment it is.

Author(s): Allie Craddock, Casie Peng 

"""
###############

class Room:
    """
    This is the constructor for the Room class object. It specifies the room type (the
    specific environment the scan took place in) and an internal list of trials (dataframe objects).
    """
    def __init__(self, room_type: str):
        self.environment = room_type
        self.trials = []