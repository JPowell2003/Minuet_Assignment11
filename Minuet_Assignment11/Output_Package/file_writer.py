# Jay
# Write the cleaned data
# Write the Pepsi rows
# Logs how many records were written and how many were cleaned
# Ensure columns match original format

import pandas as pd

class FileWriter:
    def __init__(self, cleaned_df, anomalies_df):
        self.cleaned_df = cleaned_df
        self.anomalies_df = anomalies_df

    def write_cleaned_data(self, filepath="cleanedData.csv"):
        self.cleaned_df.to_csv(filepath, index=False)
        print("Cleaned data written to '{}'".format(filepath))
        print("Rows written: {}".format(len(self.cleaned_df)))

    def write_anomalies(self, filepath="dataAnomalies.csv"):
        self.anomalies_df.to_csv(filepath, index=False)
        print("Anomaly data written to '{}'".format(filepath))
        print("Rows written: {}".format(len(self.anomalies_df)))

    def get_row_counts(self):
        return {
            "cleaned_rows": len(self.cleaned_df),
            "pepsi_rows": len(self.anomalies_df)
        }

    def validate_columns(self, reference_columns):
        for df_name in ["cleaned_df", "anomalies_df"]:
            df = getattr(self, df_name)
            for col in reference_columns:
                if col not in df.columns:
                    df[col] = None
            df = df[reference_columns]
            setattr(self, df_name, df)