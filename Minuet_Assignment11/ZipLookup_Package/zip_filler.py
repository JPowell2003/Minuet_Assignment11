# Shantele
# Looks up ZIP codes using the API
# Only fills in ZIPs for the first 5 missing
# Pulls a random ZIP from the results if multiples exist
# Identifies rows with missing ZIPS (just tags them doesn't fill them)

import requests

class ZipFiller:
    def __init__(self, dataframe):
        self.data = dataframe 
        self.api_key = "9c401f50-1a1f-11f0-9e9c-b3ffac1ed18c"
        self.api_url = "https://app.zipcodebase.com/api/v1/search"

    def find_missing_zip_rows(self, limit=5):
        """
        Finds up to `limit` rows with missing ZIP codes in 'Full Address'.
        Returns a list of (index, address) tuples (not extracting city here).
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
        """Checks if the address string contains a ZIP code (any digit in last 6 chars)."""
        return any(char.isdigit() for char in address[-6:])

    def extract_city(self, address):
        """
        Extracts city from the address string – assumes it's second to last comma-separated item.
        """
        parts = address.split(",")
        if len(parts) >= 2:
            return parts[-2].strip()
        return None

    def get_zip_for_city(self, city, country="US"):
        """
        Uses the API to retrieve ZIP codes for a given city.
        Returns a list of ZIP codes (strings), or an empty list.
        """
        params = {
            "apikey": self.api_key,
            "city": city,
            "country": country
        }

        try:
            response = requests.get(self.api_url, params=params)
            if response.status_code == 200:
                data = response.json()
                return data.get("results", {}).get(city, [])
            else:
                print(f"API error {response.status_code}: {response.text}")
        except Exception as e:
            print(f"API request failed: {e}")

        return []
