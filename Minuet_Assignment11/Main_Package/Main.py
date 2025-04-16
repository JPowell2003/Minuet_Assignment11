#Imports all the classes

import sys
import os
import pandas as pd

from Input_Package.file_loader import FileLoader
from Clean_Package.clean import *

if __name__ == "__main__":
    # Set path to your CSV file
    file_path = "Data/fuelPurchaseData.csv"

    # Load the data from CSV
    loader = FileLoader(file_path)
    raw_data = loader.load_csv()

    if raw_data is None:
        print("No data loaded. Exiting.")
    else:
        # Initialize the Cleaner with raw data
        cleaner = Cleaner(raw_data)

        # Remove duplicates from file (optional if you want this right away)
        cleaner.remove_duplicates(file_path)

        # Format price and separate Pepsi
        cleaner.format_gross_price()
        cleaner.separate_pepsi_purchase()

        # Get cleaned and anomaly data
        clean_df = cleaner.get_clean_data()
        pepsi_df = cleaner.get_anomalies()

        # DEBUG PRINT: Show sample of each
        print("CLEANED DATA SAMPLE:")
        print(clean_df.head(6))

        print("PEPSI PURCHASES SAMPLE:")
        print(pepsi_df.head(6))



