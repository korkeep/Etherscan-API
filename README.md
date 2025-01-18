# Etherscan API for Tracking Malicious Developers 🪙

## Overview

The Etherscan API provides a wide range of data that can be leveraged to trace and identify **malicious token developers**. This includes data related to transactions, token transfers, contract interactions, and account activities. Through this project, we can identify addresses involved in malicious activities and track them effectively.

## Tracking Malicious Token Developers

To track malicious token developers, we focus on detecting abnormal or suspicious patterns:

1. **Abnormal Token Issuance and Transfers**: **`analyze_token.py`**
    - **Excessive token issuance**: Track developers who rapidly issue large quantities of tokens.
    - **Suspicious transfers**: Detect token transfers to or from suspicious addresses, which might indicate fraud or market manipulation.

    Use **`action=tokennfttx`** or **`action=tokentx`** to track token transfers and identify abnormal activities.

2. **Smart Contract ABI and Source Code Analysis**: **`analyze_contract.py`**
    - **Malicious contract code**: Identify smart contracts with functions that might exploit users or steal funds.
    - **Risky contracts**: Contracts that encourage users to deposit large amounts of funds with little transparency or return.

    Use **`action=getsourcecode`** or **`action=getabi`** to analyze the source code and ABI of the contracts and look for suspicious code.

3. **Transaction Patterns**: **`analyze_transaction.py`**
    - **Excessive transactions**: Track addresses that are making numerous transactions in a short period.
    - **Suspicious transaction activity**: Identify addresses making abnormal token transfers or engaging in token pumping and dumping activities.

    Use **`action=txlist`** to check transaction history for abnormal behavior.

4. **Token Holder List**: **`analyze_holder.py`**
    - **Non-transparent holder structure**: Track token developers who are distributing large quantities of tokens to a few specific addresses, potentially leading to market manipulation.

    Use **`action=tokenholder`** to get the list of token holders and analyze the distribution patterns.