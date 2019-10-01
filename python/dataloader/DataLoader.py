import os
import numpy as np
import random
import glob



class DataLoader:

    def __init__(self, frame_count):
        self.data_path = # create path to dataset from dataloader file
        self.data = [] # this is where we will append all our data
        self.frame_count = frame_count

    """
    def find_data_path(self):
        Possible helper function for self.data_path to make cleaner code
        Can return path in this function
    """

    def load_data(self, year, month, day):
        """
        This function should append all image data from given time stamps
        to self.data. You can assume year, month and day in following format:
        "2009", "01", "01". But better to make a check if data available for
        give date. You'll need os functions. Also look into glob to retrieve
        all data in a folder. NOTE!!!: We need to append a nested list because
        we need each time sequences to be seperate:
        [[pic 1, pic 2, pic3], [pic4, pic5, pic6]].
        If num_pics % self.frame_count != 0 then just ignore last few images
        to ensure uniform length of time sequences.
        """
        # Recursively glob through data path
        num_files = 0
        data = []
        for path in glob.glob(f"{self.data_path}/{year}/{month}/{day}", recursive=False):
            # Ensure valid path
            if not os.path.isfile(path):
                continue

            # Read file into memory and append to data
            num_files += 1
            with open(path, 'rb') as fp:
                data.append(fp.read())

        # Append generated list to class data
        if data:
            self.data.append(data)

        # Return number of files we were able to parse so we can check if any data were retrieved
        return num_files


    def get_all_data():
        """This function should get all weather data currently in the dataset"""


    def random_shuffle(self):
        """
        We need this function to randomly shuffle self.data. I think random
        should have a function for this but not sure.
        """


    def get_batch(self, size):
        """
        This function should return a batch of 'size' random time sequences
        """

"""
Whatever you want this file to run (if you want to test), you can write your
code below this function and when running on terminal it will execute.
if __name__ == "__main__":


    """
