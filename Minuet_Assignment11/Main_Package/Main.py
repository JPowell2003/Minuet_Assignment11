#Imports all the classes

import sys
import os
import pandas as pd

from Input_Package.file_loader import FileLoader
from Clean_Package.clean import *
from ZipLookup_Package.zip_filler import ZipFiller

if __name__ == "__main__":
    file_path = "Data/fuelPurchaseData.csv"

    loader = FileLoader(file_path)
    raw_data = loader.load_csv()

    cleaner = Cleaner(raw_data)

    cleaner.remove_duplicates(file_path)

    cleaner.format_gross_price()
    cleaner.separate_pepsi_purchase()

    clean_df = cleaner.get_clean_data()
    pepsi_df = cleaner.get_anomalies()

    print("CLEANED DATA SAMPLE:")
    print(clean_df.head(6))

    print("\nPEPSI PURCHASES SAMPLE:")
    print(pepsi_df.head(6))

    zip_filler = ZipFiller(clean_df)

    missing = zip_filler.find_missing_zip_rows(limit=5)
    print("\nRows with missing ZIP codes:")
    for index, address in missing:
        print(f"Row {index} - {address}")

    zip_filler.fill_missing_zips(limit=5)

    updated_data = zip_filler.get_updated_data()

    print("\nUPDATED CLEANED DATA SAMPLE:")
    print(updated_data.head(6).to_string(index=False))

    updated_data.to_csv("updated_data.csv", index=False)
    print("\nUpdated data saved to 'updated_data.csv'")
