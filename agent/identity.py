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

if __name__ == "__main__":
    agent = AIAgent()
    agent.create_new_identity()