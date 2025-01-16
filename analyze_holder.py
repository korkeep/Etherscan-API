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

# Function to get the list of token holders for a given token contract
def get_token_holder_list(token_address):
    # API request parameters
    params = {
        'module': 'token',
        'action': 'tokenholderlist',
        'contractaddress': token_address,
        'page': 1,
        'offset': 100,  # Number of holders to fetch per request (can adjust)
        'apikey': API_KEY
    }

    # Send GET request to the Etherscan API
    response = requests.get(BASE_URL, params=params)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        if data['status'] == '1':  # '1' indicates a successful API call
            return data['result']  # Return the list of token holders
        else:
            print(f"Error: {data['message']}")
            return None
    else:
        print("Error: Failed to fetch token holder list from Etherscan")
        return None

# Function to analyze token holder distribution
def analyze_token_holders(token_address):
    # Get the list of token holders
    holders = get_token_holder_list(token_address)
    
    if holders:
        print(f"Token Holder List for token address {token_address}:")
        
        # Example analysis: Check the distribution of token holders
        total_holders = len(holders)
        large_holders_count = sum(1 for holder in holders if int(holder['balance']) > 1000000000000000000000)  # More than 1000 tokens (in smallest unit)
        
        print(f"Total holders: {total_holders}")
        print(f"Holders with more than 1000 tokens: {large_holders_count}")
        
        # Example: Check for top holders (you can sort the holders by balance)
        top_holders = sorted(holders, key=lambda x: int(x['balance']), reverse=True)[:5]
        print("\nTop 5 token holders by balance:")
        for i, holder in enumerate(top_holders, 1):
            print(f"{i}. Address: {holder['address']}, Balance: {holder['balance']}")
    else:
        print("No token holder data available.")

# Run the analysis
analyze_token_holders(TARGET_ADDRESS)
