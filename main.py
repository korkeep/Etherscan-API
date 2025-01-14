import os
from dotenv import load_dotenv
import requests

# Get API_KEY from .env
load_dotenv()
API_KEY = os.getenv('ETHERSCAN_API_KEY')
BASE_URL = 'https://api.etherscan.io/api'
TARGET_ADDRESS = os.getenv('TARGET_ADDRESS')

# get_history: Get a list of ERC20 Token Transfer Events by Address
def get_history(address):

    url = f'{BASE_URL}?module=account&action=tokennfttx&address={address}&apikey={API_KEY}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        if data['status'] == '1':
            transactions = data['result']
            
            if transactions:
                print(f'Token Creator: {address}')
                
                print(f"Index | Token Name | Token Symbol | Amount | Block | Timestamp")
                for idx, tx in enumerate(transactions, 1):
                    token_name = tx.get('tokenName', 'N/A')  # Default to 'N/A' if not found
                    token_symbol = tx.get('tokenSymbol', 'N/A')  # Default to 'N/A' if not found
                    value = tx.get('value', 'N/A')  # Default to 'N/A' if 'value' is missing
                    block_number = tx.get('blockNumber', 'N/A')  # Default to 'N/A' if not found
                    timestamp = tx.get('timeStamp', 'N/A')  # Default to 'N/A' if not found                    
                    print(f"{idx} | {token_name} | {token_symbol} | {value} | {block_number} | {timestamp}")
            
            else:
                print(f'Token Creator: {address}')
                print(f"No token transaction history found.")
        
        else:
            print(f"API Call Error: {data['message']}")
    
    else:
        print(f"HTTP Request Error: {response.status_code}")

# Target Address to trace
address = TARGET_ADDRESS
get_history(address)
