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

# Function to get the ABI of a smart contract
def get_contract_abi(address):
    # API request parameters
    params = {
        'module': 'contract',
        'action': 'getabi',
        'address': address,
        'apikey': API_KEY
    }

    # Send GET request to the Etherscan API
    response = requests.get(BASE_URL, params=params)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        if data['status'] == '1':  # '1' indicates a successful API call
            return json.loads(data['result'])  # Return the ABI in JSON format
        else:
            print(f"Error: {data['message']}")
            return None
    else:
        print("Error: Failed to fetch ABI from Etherscan")
        return None

# Function to get the source code of a smart contract
def get_contract_source_code(address):
    # API request parameters
    params = {
        'module': 'contract',
        'action': 'getsourcecode',
        'address': address,
        'apikey': API_KEY
    }

    # Send GET request to the Etherscan API
    response = requests.get(BASE_URL, params=params)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        if data['status'] == '1':  # '1' indicates a successful API call
            return data['result'][0]['SourceCode']  # Return the source code
        else:
            print(f"Error: {data['message']}")
            return None
    else:
        print("Error: Failed to fetch source code from Etherscan")
        return None

# Function to analyze the contract ABI and source code
def analyze_contract(address):
    # Get the contract ABI
    abi = get_contract_abi(address)
    if abi:
        print(f"Contract ABI for address {address}:")
        print(json.dumps(abi, indent=2))
    
    # Get the contract source code
    source_code = get_contract_source_code(address)
    if source_code:
        print(f"\nContract Source Code for address {address}:")
        print(source_code)

    # Example analysis: Check if the contract contains any suspicious functions
    if abi:
        suspicious_functions = ['selfdestruct', 'suicide']  # Example of suspicious functions
        for function in suspicious_functions:
            if any(function in str(item) for item in abi):
                print(f"Suspicious function '{function}' found in the contract ABI!")

# Example address to analyze
address = TARGET_ADDRESS

# Run the analysis
analyze_contract(address)
