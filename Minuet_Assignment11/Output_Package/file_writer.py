# Jay
# Write the cleaned data
# Write the Pepsi rows
# Logs how many records were written and how many were cleaned
# Ensure columns match original format

class FileWriter:
    def __init__(self, cleaned_df, anomalies_df):
        '''
        Store the cleaned and anomaly data for writing
        '''

    def write_cleaned_data(self, filepath):
        '''
        Writes the cleaned fuel data to 'cleanedData.csv'
        Logs how many rows were written
        '''

    def write_anomalies(self, filepath):
        '''
        Writes the Pepsi anomalies to 'dataAnomalies.csv'
        Logs how many rows were written
        '''

    def get_row_counts(self):
        '''
        Returns a dictionary or tuple with counts of total cleaned rows and total pepsi rows
        '''

    def validate_columns(self, reference_columns):
        '''
        Ensures that the cleaned and anomaly data use the same columns
        as the original input file. Reorders or fills columns if necessary
        '''