# Shantele
# Looks up ZIP codes using the API
# Only fills in ZIPs for the first 5 missing
# Pulls a random ZIP from the results if multiples exist
# Identifies rows with missing ZIPS (just tags them doesn't fill them)

import requests

class ZipFiller:
    def __init__(self, dataframe):
        """
        Initializes ZipFiller with the cleaned DataFrame and hardcoded API credentials.
        """
        self.data = dataframe 
        self.api_key = "9c401f50-1a1f-11f0-9e9c-b3ffac1ed18c"
        self.api_url = "https://app.zipcodebase.com/api/v1/code/city"

    def find_missing_zip_rows(self, limit=5):
        """
        Finds up to `limit` rows with missing ZIP codes in 'Full Address'.
        Returns a list of (index, address) tuples.
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
        Checks if the address string contains a ZIP code (any digit in last 6 chars).
        """
        return any(char.isdigit() for char in address[-6:])

    def extract_city(self, address):
        """
        Tries to extract a likely city name from a messy address string using plain Python.
        """
        parts = [p.strip() for p in address.split(",") if p.strip()]
 
        for part in parts:
            # Skip parts that contain any digits
            if any(char.isdigit() for char in part):
                continue
            # Skip 2-letter states like 'OH'
            if len(part) == 2 and part.isupper():
                continue
            # If it's all alphabetic or has spaces, it's likely a city
            if all(char.isalpha() or char.isspace() for char in part):
                return part
 
        # Fallback: return second-to-last part if available
        if len(parts) >= 2:
            return parts[-2]
 
        return None

    def get_zip_for_city(self, city, state="OH", country="US"):
        """
        Uses the API to retrieve ZIP codes for a given city.
        Requires city, state, and country to be passed in.
        Returns a list of ZIP code dictionaries (may include multiple).
        Example: [{'postal_code': '44105'}, {'postal_code': '44106'}]
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
        Finds missing ZIPs and updates 'Full Address' for up to `limit` rows.
        Only appends the first ZIP returned by the API.
        """
        missing_rows = self.find_missing_zip_rows(limit=limit)

        for index, address in missing_rows:
            city = self.extract_city(address)
            if city:
                zips = self.get_zip_for_city(city, state="OH")
                if zips:
                    zip_code = zips[0] #.get("postal_code")
                    if zip_code:
                        updated_address = f"{address.strip()} {zip_code}"
                        self.data.at[index, "Full Address"] = updated_address

    def get_updated_data(self):
        """
        Returns the updated DataFrame with ZIPs filled.
        """
        return self.data

