#Imports all the classes

import sys
import os
import pandas as pd

from Input_Package.file_loader import FileLoader
from Clean_Package.clean import *
from ZipLookup_Package.zip_filler import ZipFiller

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

       
        zip_filler = ZipFiller(clean_df)
        missing = zip_filler.find_missing_zip_rows(limit=5)

        print("Rows with missing ZIP codes:")
        for index, address in missing:
            city = zip_filler.extract_city(address)
            if city:
                zip_codes = zip_filler.get_zip_for_city(city)
                print("Row", index)
                print("  Address:", address)
                print("  City:", city)
                print("  ZIP Codes:", zip_codes)
            else:
                print("Row", index)
                print("  Address:", address)
                print("  City not found")

              

                # Fill missing ZIP codes
                zip_filler.fill_missing_zips(limit=5)

                # Get updated data
                updated_data = zip_filler.get_updated_data()

                # Print updated data
                print(updated_data)

                # Optionally, save it back to a file
                updated_data.to_csv("updated_data.csv", index=False)



