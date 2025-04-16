# Shantele
# Looks up ZIP codes using the API
# Only fills in ZIPs for the first 5 missing
# Pulls a random ZIP from the results if multiples exist
# Identifies rows with missing ZIPS (just tags them doesn't fill them)

class APIGetter:
    def __init__(self, dataframe):
        self.data = dataframe 
        self.api_key = "9c401f50-1a1f-11f0-9e9c-b3ffac1ed18c"
        self.api_url = "https://app.zipcodebase.com/api/v1/search"
