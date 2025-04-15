#Imports all the classes

from Input_Package.file_loader import FileLoader 



if __name__ == "__main__":
    
    file_path = "data/fuelPurchaseData.csv"  # Adjust path if necessary
    loader = FileLoader(file_path)

    # Load and print the CSV data
    data = loader.load_csv()
    print("CSV Data Loaded Successfully:")
       
 


