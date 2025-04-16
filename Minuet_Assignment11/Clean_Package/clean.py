# Jay
# Drop Duplicate rows: https://www.geeksforgeeks.org/python-pandas-dataframe-drop_duplicates/
# Remove Pepsi purchases and save them seperately: https://www.geeksforgeeks.org/how-to-drop-rows-in-dataframe-by-conditions-on-column-values/
# Format Gross Price to 2 decimal places: https://sparkbyexamples.com/pandas/pandas-dataframe-round-method/

import pandas as pd

class Cleaner:
    def __init__(self,raw_data):
        '''
        Initialize the Cleaner with raw data from FileLoader.
        Converts list of dictionaries to a DataFrame and prepares it for cleaning.
        '''
        self.data = pd.DataFrame(raw_data)
        self.cleaned_data = None
        self.anomalies = None

    def remove_duplicates(self, filepath):
        '''
        Removes duplicate rows from the dataset and updates internal DataFrame
        '''
        df = pd.read_csv(filepath)
        df_cleaned = df.drop_duplicates()
        df_cleaned.to_csv(filepath, index=False)

    def separate_pepsi_purchase(self):
        '''
        Splits the Dataframe between valid fuel purchases and Pepsi then stores them both
        '''
        if "Fuel Type" in self.data.columns:
            self.anomalies = self.data[self.data["Fuel Type"] == "Pepsi"]
            self.cleaned_data = self.data[self.data["Fuel Type"] != "Pepsi"]
        else:
            self.cleaned_data = self.data.copy()
            self.anomalies = pd.DataFrame()

    def format_gross_price(self):
        '''
        Formats the Gross Pay column to two decimal places
        '''
        if "Gross Price" in self.data.columns:
           self.data["Gross Price"] = pd.to_numeric(self.data["Gross Price"], errors="coerce")
    
    def get_clean_data(self):
        '''
        Returns the clean fuel purchase dataframe
        '''
        return self.cleaned_data if self.cleaned_data is not None else self.data

    def get_anomalies(self):
        '''
        Returns the Pepsi purchases data frame
        '''
        return self.anomalies if self.anomalies is not None else pd.DataFrame()
