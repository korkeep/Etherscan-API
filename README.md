# Etherscan API for Tracking Malicious Developers 🪙

## Table of Contents
1. [Overview](#overview)
2. [Key Features](#key-features)
   - [analyze_token.py: Abnormal Token Issuance and Transfers](https://github.com/korkeep/Etherscan-API/blob/main/analyze_token.py)
   - [analyze_contract.py: Smart Contract ABI and Source Code Analysis](https://github.com/korkeep/Etherscan-API/blob/main/analyze_contract.py)
   - [analyze_transaction.py: Transaction Patterns](https://github.com/korkeep/Etherscan-API/blob/main/analyze_transaction.py)
   - [analyze_holder.py: Token Holder List](https://github.com/korkeep/Etherscan-API/blob/main/analyze_holder.py)
3. [Setup & Run](#setup--run)
4. [Notes](#notes)

## Overview

The Etherscan API provides a wide range of data that can be leveraged to trace and identify **malicious token developers**. This includes data related to transactions, token transfers, contract interactions, and account activities. Through this project, we can identify addresses involved in malicious activities and track them effectively.

## Key Features

### 1. **`analyze_token.py`: Abnormal Token Issuance and Transfers**
Track excessive token issuance or suspicious transfers.

- **Usage**: Use **`action=tokennfttx`** or **`action=tokentx`** to track token transfers.
- **Key Focus**: Identify suspicious behavior, such as high-frequency transfers or large transactions.

```python
# Example: Tracking token transfers
def get_token_transfers(address, action='tokentx'):
    # API call to fetch token transfer data
    pass
```

### 2. **`analyze_contract.py`: Smart Contract ABI and Source Code Analysis**
Analyze smart contracts for suspicious or malicious code.

- **Usage**: Use **`action=getabi`** or **`action=getsourcecode`** to fetch ABI or source code.
- **Key Focus**: Look for risky contract functions that may harm users.

```python
# Example: Fetching contract ABI
def get_contract_abi(address):
    # API call to fetch contract ABI
    pass
```

### 3. **`analyze_transaction.py`: Transaction Patterns**
Identify abnormal transaction patterns, including high-frequency and high-value transactions.

- **Usage**: Use **`action=txlist`**  to retrieve transaction history.
- **Key Focus**: Detect suspicious behavior, like token pumping or frequent transfers.

```python
# Example: Analyzing transaction history
def get_transaction_history(address):
    # API call to fetch transaction data
    pass
```

### 4. **`analyze_holder.py`: Token Holder List**
Analyze the distribution of token holders to identify potential market manipulation.

- **Usage**: Use **`action=tokenholder`**  to retrieve token holder information.
- **Key Focus**: Identify centralized holder structures and large token concentrations.

```python
# Example: Analyzing token holders
def get_token_holder_list(token_address):
    # API call to fetch token holder data
    pass
```

## Setup & Run

### 1. Set Up the Environment

Before using any of the features, ensure you have your Etherscan API key set up. Store it securely in a `.env` file:

```text
ETHERSCAN_API_KEY=your_api_key_here
```

### 2. Install Necessary Libraries

Instead of installing libraries individually, you can save the required libraries in a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 3. Run the Script

Run the corresponding script to fetch and analyze the relevant data:

```bash
python analyze_[NAME].py
```
> **Note**: Replace `[NAME]` with the specific script name, such as `token`, `contract`, `transaction`, or `holder`.


## Notes
- Replace `your_api_key_here` with your actual Etherscan API key.
- Refer to the respective Python script (`analyze_token.py`, `analyze_contract.py`, etc.) for full implementations.
- Ensure you handle API rate limits and errors appropriately for optimal usage.
