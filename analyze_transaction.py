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

# Function to get transaction history for a given address
def get_transaction_history(address, start_block=0, end_block=99999999):
    # API request parameters
    params = {
        'module': 'account',
        'action': 'txlist',  # Use 'txlist' to fetch normal transaction history
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
        print("Error: Failed to fetch transaction history from Etherscan")
        return None

# Function to analyze transaction patterns for a given address
def analyze_transaction_patterns(address):
    # Get the transaction history
    transactions = get_transaction_history(address)
    
    if transactions:
        # Example analysis: Track the number of transactions over a certain amount
        threshold = 1000000000000000000  # 1 ETH (in Wei)
        high_value_tx_count = 0
        
        # Analyze each transaction
        for tx in transactions:
            # Check if the value of the transaction is greater than the threshold
            if int(tx['value']) >= threshold:
                high_value_tx_count += 1
        
        # Print the analysis result
        print(f"Transaction Pattern Analysis for address {address}:")
        print(f"Total transactions: {len(transactions)}")
        print(f"High-value transactions (greater than 1 ETH): {high_value_tx_count}")
        
        # Example: Check for frequent transaction initiations or suspicious patterns
        if high_value_tx_count > 5:  # Threshold for suspiciously frequent high-value transactions
            print(f"Warning: High frequency of large transactions detected!")
    else:
        print("No transaction data available.")

# Run the analysis
analyze_transaction_patterns(TARGET_ADDRESS)
