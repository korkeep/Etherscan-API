import os
from dotenv import load_dotenv
import requests
import json

# Load API key and target address from .env file
load_dotenv()
API_KEY = os.getenv('ETHERSCAN_API_KEY')
TARGET_ADDRESS = os.getenv('TARGET_ADDRESS')

# Etherscan API endpoint
BASE_URL = 'https://api.etherscan.io/api'

# Function to get token transfers for a given address
def get_token_transfers(address, start_block=0, end_block=99999999, action='tokentx'):
    # API request parameters
    params = {
        'module': 'account',
        'action': action,  # 'tokentx' for standard token transfers, 'tokennfttx' for NFT transfers
        'address': address,
        'startblock': start_block,
        'endblock': end_block,
        'sort': 'desc',  # Sort transactions in descending order (most recent first)
        'apikey': API_KEY
    }

    # Send GET request to the Etherscan API
    response = requests.get(BASE_URL, params=params)
    
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        if data['status'] == '1':  # '1' indicates a successful API call
            return data['result']  # Return the list of transactions
        else:
            print(f"Error: {data['message']}")
            return None
    else:
        print("Error: Failed to fetch data from Etherscan")
        return None

# Function to analyze the token transfers and identify abnormal activities
def analyze_abnormal_token_activity(address):
    transactions = get_token_transfers(address)
    
    if transactions:
        abnormal_transactions = []
        
        # Iterate through the transactions and look for abnormal behavior
        for tx in transactions:
            # Example condition: Look for transactions with unusually large amounts
            if float(tx['value']) > 1000000:  # Adjust the threshold as needed
                abnormal_transactions.append(tx)
        
        # Print abnormal transactions
        if abnormal_transactions:
            print(f"Abnormal token transactions for address {address}:")
            for tx in abnormal_transactions:
                print(json.dumps(tx, indent=2))
        else:
            print(f"No abnormal transactions found for address {address}.")
    else:
        print("No token transfer data available.")

# Example address to analyze
address = TARGET_ADDRESS

# Run the analysis
analyze_abnormal_token_activity(address)