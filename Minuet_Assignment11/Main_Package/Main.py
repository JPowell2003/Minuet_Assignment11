import sys
import pandas as pd

from Input_Package.file_loader import FileLoader
from Clean_Package.clean import *
from ZipLookup_Package.zip_filler import ZipFiller
from Output_Package.file_writer import FileWriter

if __name__ == "__main__":
    file_path = "Data/fuelPurchaseData.csv"
    output_cleaned_path = "Data/cleanedData.csv"
    output_anomalies_path = "Data/dataAnomalies.csv"

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

    print("PEPSI PURCHASES SAMPLE:")
    print(pepsi_df.head(6))

    zip_filler = ZipFiller(clean_df)

    missing = zip_filler.find_missing_zip_rows(limit=5)
    print("Rows with missing ZIP codes:")
    for index, address in missing:
        print("Row {} - {}".format(index, address))

    zip_filler.fill_missing_zips(limit=5)

    updated_data = zip_filler.get_updated_data()

    print("UPDATED CLEANED DATA SAMPLE:")
    print(updated_data.head(6).to_string(index=False))

    writer = FileWriter(updated_data, pepsi_df)

    original_columns = list(raw_data[0].keys()) if raw_data else []
    writer.validate_columns(original_columns)

    writer.write_cleaned_data(filepath=output_cleaned_path)
    writer.write_anomalies(filepath=output_anomalies_path)

    counts = writer.get_row_counts()
    print("Total cleaned rows:", counts["cleaned_rows"])
    print("Total Pepsi rows:", counts["pepsi_rows"])
