# File Name : Minuet_Assignment11
# Student Name: Shantele King
# email:  King4sl@mail.uc.edu
# Assignment Number: Assignment11
# Due Date: 04/17/2025
# Course #/Section:  4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: In this assignment we made eddits to a csv file and then ran code to present the final changes and reqiured information wanted from the data set.
# Brief Description of what this module does: This moduel uploads the csv file to our application
# Citations:ChatGPT
# Anything else that's relevant: N/A


import csv

class FileLoader:

      
    def __init__(self, file_path):

        """
        Initializes the fileloader with the specified path.
        @param: the path to the CSV file 
        """
        self.file_path = file_path

      
    def load_csv(self):
        """
        Loads the CSV file and returns its contents as a list of dictionaries.
        @return: A list of dictionaries representing the CSV data, or None if loading fails.
        """
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

