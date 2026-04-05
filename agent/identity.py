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
        
        # Load the private key from .env
        self.private_key = os.getenv('AGENT_PRIVATE_KEY')
        
        if self.private_key:
            self.account = Account.from_key(self.private_key)
            print(f"✅ AGENT LOADED: {self.account.address}")
        else:
            self.account = None
            print("⚠️ NO AGENT KEY FOUND. Run create_new_identity() to generate one.")

    def create_new_identity(self):
        """Generates a fresh wallet for the AI"""
        new_acc = self.w3.eth.account.create()
        print(f"✨ NEW AGENT BORN")
        print(f"Address: {new_acc.address}")
        print(f"Private Key: {new_acc.key.hex()}")
        print("-" * 30)
        print("ACTION REQUIRED: Save this key in your .env file as 'AGENT_PRIVATE_KEY'")

    def send_transaction(self, to_address, amount_eth):
        """Signs and sends a transaction with Gas Guard protection"""
        if not self.account:
            return "ERROR: No account loaded."

        try:
            # 1. Prepare Transaction Details
            nonce = self.w3.eth.get_transaction_count(self.account.address)
            gas_price = self.w3.eth.gas_price
            
            # --- FAANG GRADE: THE GAS GUARD ---
            # Don't send if gas is higher than 50 Gwei (prevents wasting your ETH)
            max_gas_allowed = self.w3.to_wei(50, 'gwei')
            if gas_price > max_gas_allowed:
                print(f"⚠️ GAS TOO HIGH: {self.w3.from_wei(gas_price, 'gwei')} Gwei. Aborting.")
                return "CANCELLED_GAS_HIGH"

            tx = {
                'nonce': nonce,
                'to': to_address,
                'value': self.w3.to_wei(amount_eth, 'ether'),
                'gas': 21000, 
                'gasPrice': gas_price,
                'chainId': 11155111 # Sepolia
            }

            # 2. Sign Locally (Sovereign signing)
            signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)

            # 3. Broadcast
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.raw_transaction)
            
            print(f"🚀 TX SENT! Hash: {self.w3.to_hex(tx_hash)}")
            return self.w3.to_hex(tx_hash)

        except Exception as e:
            print(f"❌ BLOCKCHAIN ERROR: {e}")
            return f"ERROR_{str(e)}"

if __name__ == "__main__":
    agent = AIAgent()
    # If you don't have a key yet, uncomment the line below:
    # agent.create_new_identity()