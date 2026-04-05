import os
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv

# Load secrets from .env file
load_dotenv()

class AIAgent:
    def __init__(self):
        # Connect to a public testnet node
        self.w3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth_sepolia'))
        self.account = None

    def create_new_identity(self):
        """Generates a fresh wallet for the AI"""
        self.account = self.w3.eth.account.create()
        print(f"NEW AGENT BORN")
        print(f"Address: {self.account.address}")
        print(f"Private Key: {self.account.key.hex()}")
        print("-" * 30)
        print("SAVE THIS KEY IN YOUR .env FILE AS 'AGENT_PRIVATE_KEY'")

def send_transaction(self, to_address, amount_eth):
        """Signs and sends a transaction to the network"""
        if not self.account:
            return "No account loaded."

        # 1. Prepare the transaction details
        nonce = self.w3.eth.get_transaction_count(self.account.address)
        gas_price = self.w3.eth.gas_price
        
        tx = {
            'nonce': nonce,
            'to': to_address,
            'value': self.w3.to_wei(amount_eth, 'ether'),
            'gas': 21000, # Standard ETH transfer gas limit
            'gasPrice': gas_price,
            'chainId': 11155111 # Sepolia Testnet ID
        }

        # 2. Sign the transaction locally (Sovereign move!)
        signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)

        # 3. Broadcast to the world
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        
        print(f"🚀 Transaction Sent! Hash: {self.w3.to_hex(tx_hash)}")
        return self.w3.to_hex(tx_hash)

if __name__ == "__main__":
    agent = AIAgent()
    agent.create_new_identity()