# Shantele
# Reads the csv into a list of dictionaries
# Handles proper CSV reading


import csv

class FileLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_csv(self):
        """Loads a CSV file and returns a list of dictionaries."""
        try:
            with open(self.file_path, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]  # Convert to list of dictionaries
            return data
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} was not found.")
            return None
        except Exception as e:
            print(f"Error loading CSV file: {e}")
            return None

