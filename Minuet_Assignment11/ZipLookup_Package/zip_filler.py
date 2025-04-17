# File Name : Minuet_Assignment11
# Student Name: Shantele King
# email:  King4sl@mail.uc.edu
# Assignment Number: Assignment11
# Due Date: 04/17/2025
# Course #/Section:  4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: In this assignment we made eddits to a csv file and then ran code to present the final changes and reqiured information wanted from the data set.
# Brief Description of what this module does: This moduel retrieves the API and trys to match Zipcoads with given cities.
# Citations: ChatGPT 
# Anything else that's relevant: N/A


import requests

class ZipFiller:
    """
    A class to fill in missing ZIP codes in addresses using a city-based ZIP code API.

    Attributes:
        data (pandas.DataFrame): The DataFrame containing address data.
        api_key (str): API key for the ZIP code API.
        api_url (str): The endpoint URL for ZIP code lookup.
    """

    def __init__(self, dataframe):
        """
        Initializes ZipFiller with the cleaned DataFrame and hardcoded API credentials.

        @param dataframe: A pandas DataFrame containing a 'Full Address' column.
        @type dataframe: pandas.DataFrame
        """
        self.data = dataframe 
        self.api_key = "9c401f50-1a1f-11f0-9e9c-b3ffac1ed18c"
        self.api_url = "https://app.zipcodebase.com/api/v1/code/city"

    def find_missing_zip_rows(self, limit=5):
        """
        Finds rows with missing ZIP codes in the 'Full Address' column.
        @param: The maximum number of rows to return. Default is 5.
        @return: A list of tuples containing (index, address) for missing ZIPs.
   
        """
        missing_rows = []

        for index, row in self.data.iterrows():
            address = row.get("Full Address", "")
            if isinstance(address, str) and not self.has_zip_code(address):
                missing_rows.append((index, address))
            if len(missing_rows) >= limit:
                break

        return missing_rows

    def has_zip_code(self, address):
        """
        Checks whether the given address string contains a ZIP code.

        @param address: The address string to check.
        @return: True if the address contains a ZIP code, False otherwise.
        """
        return any(char.isdigit() for char in address[-6:])

    def extract_city(self, address):
        """
        Extracts a probable city name from a given address string.

        @param address: The messy address string.
        @return: The extracted city name, or None if not found.
        """
        parts = [p.strip() for p in address.split(",") if p.strip()]
 
        for part in parts:
            if any(char.isdigit() for char in part):
                continue
            if len(part) == 2 and part.isupper():
                continue
            if all(char.isalpha() or char.isspace() for char in part):
                return part

        if len(parts) >= 2:
            return parts[-2]
 
        return None

    def get_zip_for_city(self, city, state="OH", country="US"):
        """
        Retrieves ZIP codes for a given city using the API.

        @param city: The city name to look up.
        @param state: The state abbreviation (default "OH").
        @param country: The country code (default "US").
        @return: A list of ZIP code dictionaries (e.g., [{'postal_code': '44105'}]).
        """
        params = {
            "apikey": self.api_key,
            "city": city,
            "state": state,
            "country": country
        }

        try:
            response = requests.get(self.api_url, params=params)
            if response.status_code == 200:
                data = response.json()
                return data.get("results", [])
            else:
                print(f"API error {response.status_code}: {response.text}")
                print("Params used:", params)
        except Exception as e:
            print(f"API request failed: {e}")

        return []

    def fill_missing_zips(self, limit=5):
        """
        Finds and fills in missing ZIP codes for up to `limit` addresses.

        @param limit: The number of addresses to process. Default is 5.
        """
        missing_rows = self.find_missing_zip_rows(limit=limit)

        for index, address in missing_rows:
            city = self.extract_city(address)
            if city:
                zips = self.get_zip_for_city(city, state="OH")
                if zips:
                    zip_code = zips[0]  # Just using the first ZIP returned
                    if zip_code:
                        updated_address = f"{address.strip()} {zip_code}"
                        self.data.at[index, "Full Address"] = updated_address

    def get_updated_data(self):
        """
        Returns the updated DataFrame with ZIP codes filled in.

        @return: The updated DataFrame.
        """
        return self.data

