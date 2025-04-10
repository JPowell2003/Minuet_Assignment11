# Jay
# Drop Duplicate rows: https://www.geeksforgeeks.org/python-pandas-dataframe-drop_duplicates/
# Remove Pepsi purchases and save them seperately: https://www.geeksforgeeks.org/how-to-drop-rows-in-dataframe-by-conditions-on-column-values/
# Format Gross Price to 2 decimal places: https://sparkbyexamples.com/pandas/pandas-dataframe-round-method/

class Cleaner:
    def __init__(self,dataframe):
        '''
        Initialize with the raw DataFrame and stores original data for cleaning
        '''
        self.data = dataframe

    def remove_duplicates(self):
        '''
        Removes duplicate rows from the dataset and updates internal DataFrame
        '''

    def separate_pepsi_purchase(self):
        '''
        Splits the Dataframe between valid fuel purchases and Pepsi then stores them both
        '''

    def format_gross_price(self):
        '''
        Formats the Gross Pay column to two decimal places
        '''
    def get_clean_data(self):
        '''
        Returns the clean fuel purchase dataframe
        '''
    def get_anomalies(self):
        '''
        Returns the Pepsi purchases data frame
        '''