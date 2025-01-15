# Etherscan API for Tracking Malicious Developers 🪙

## Overview

The Etherscan API provides a wide range of data that can be leveraged to trace and identify **malicious token developers**. This includes data related to transactions, token transfers, contract interactions, and account activities. Through this project, we can identify addresses involved in malicious activities and track them effectively.

## Tracking Malicious Token Developers

To track malicious token developers, we focus on detecting abnormal or suspicious patterns:

1. **Abnormal Token Issuance and Transfers**:
    - **Excessive token issuance**: Track developers who rapidly issue large quantities of tokens.
    - **Suspicious transfers**: Detect token transfers to or from suspicious addresses, which might indicate fraud or market manipulation.

    Use **`action=tokennfttx`** or **`action=tokentx`** to track token transfers and identify abnormal activities.

2. **Smart Contract ABI and Source Code Analysis**:
    - **Malicious contract code**: Identify smart contracts with functions that might exploit users or steal funds.
    - **Risky contracts**: Contracts that encourage users to deposit large amounts of funds with little transparency or return.

    Use **`action=getsourcecode`** or **`action=getabi`** to analyze the source code and ABI of the contracts and look for suspicious code.

3. **Transaction Patterns**:
    - **Excessive transactions**: Track addresses that are making numerous transactions in a short period.
    - **Suspicious transaction activity**: Identify addresses making abnormal token transfers or engaging in token pumping and dumping activities.

    Use **`action=txlist`** to check transaction history for abnormal behavior.

4. **Token Holder List**:
    - **Non-transparent holder structure**: Track token developers who are distributing large quantities of tokens to a few specific addresses, potentially leading to market manipulation.

    Use **`action=tokenholder`** to get the list of token holders and analyze the distribution patterns.

## Example Usage for Etherscan API

### 1. Fetch ERC-20/ERC-721 Token Transfer History for a Specific Address

```python
import requests

def get_token_nft_tx_history(address, api_key):
    url = f'https://api.etherscan.io/api?module=account&action=tokennfttx&address={address}&apikey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == '1':
            transactions = data['result']
            for tx in transactions:
                print(f"Token Name: {tx['tokenName']} | From: {tx['from']} | To: {tx['to']} | Token ID: {tx['tokenID']} | Block: {tx['blockNumber']} | Timestamp: {tx['timeStamp']}")
        else:
            print(f"Error: {data['message']}")
    else:
        print(f"Request failed with status code {response.status_code}")

# Example usage
get_token_nft_tx_history(TOKEN_ADDRESS, API_KEY)
```

### 2. Fetch ERC-20 Token Transfer History for a Specific Address

```python
import requests

def get_token_tx_history(address, api_key):
    url = f'https://api.etherscan.io/api?module=account&action=tokentx&address={address}&apikey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == '1':
            transactions = data['result']
            for tx in transactions:
                print(f"Token Name: {tx['tokenName']} | Token Symbol: {tx['tokenSymbol']} | From: {tx['from']} | To: {tx['to']} | Value: {tx['value']} | Block: {tx['blockNumber']} | Timestamp: {tx['timeStamp']}")
        else:
            print(f"Error: {data['message']}")
    else:
        print(f"Request failed with status code {response.status_code}")

# Example usage
get_token_tx_history(TOKEN_ADDRESS, API_KEY)
```

### 3. Fetch the Source Code of a Smart Contract

```python
import requests

def get_contract_source_code(contract_address, api_key):
    url = f'https://api.etherscan.io/api?module=contract&action=getsourcecode&address={contract_address}&apikey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == '1':
            contract_source_code = data['result'][0]['SourceCode']
            print(f"Source Code: {contract_source_code}")
        else:
            print(f"Error: {data['message']}")
    else:
        print(f"Request failed with status code {response.status_code}")

# Example usage
get_contract_source_code(SMART_CONTRACT_ADDRESS, API_KEY)
```

### 4. Fetch the ABI of a Smart Contract
```python
import requests

def get_contract_abi(contract_address, api_key):
    url = f'https://api.etherscan.io/api?module=contract&action=getabi&address={contract_address}&apikey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == '1':
            abi = data['result']
            print(f"ABI: {abi}")
        else:
            print(f"Error: {data['message']}")
    else:
        print(f"Request failed with status code {response.status_code}")

# Example usage
get_contract_abi(SMART_CONTRACT_ADDRESS, API_KEY)
```

### 5. Fetch a List of Transactions for a Specific Address
```python
import requests

def get_transaction_list(address, api_key):
    url = f'https://api.etherscan.io/api?module=account&action=txlist&address={address}&apikey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == '1':
            transactions = data['result']
            for tx in transactions:
                print(f"Tx Hash: {tx['hash']} | From: {tx['from']} | To: {tx['to']} | Value: {tx['value']} | Block: {tx['blockNumber']} | Timestamp: {tx['timeStamp']}")
        else:
            print(f"Error: {data['message']}")
    else:
        print(f"Request failed with status code {response.status_code}")

# Example usage
get_transaction_list(TOKEN_ADDRESS, API_KEY)
```

### 6. Fetch Token Holders for a Specific ERC-20 Token
```python
import requests

def get_token_holders(contract_address, api_key):
    url = f'https://api.etherscan.io/api?module=token&action=tokenholder&contractaddress={contract_address}&apikey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == '1':
            holders = data['result']
            for holder in holders:
                print(f"Address: {holder['address']} | Balance: {holder['balance']}")
        else:
            print(f"Error: {data['message']}")
    else:
        print(f"Request failed with status code {response.status_code}")

# Example usage
get_token_holders(TOKEN_CONTRACT_ADDRESS, API_KEY)
```