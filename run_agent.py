from agent.identity import AIAgent
from agent.brain import AIAgentBrain
from agent.quant_brain import QuantBrain
import csv
import os
from datetime import datetime

def log_decision(data):
    file_path = "logs/agent_history.csv"
    file_exists = os.path.isfile(file_path)
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        fieldnames = ["timestamp", "headline", "sentiment", "price", "action", "tx_hash"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

def main():
    agent = AIAgent()
    ai_brain = AIAgentBrain()
    quant_brain = QuantBrain()
    
    # 1. Input
    news = "Global economic crisis causes markets to plummet."
    
    # 2. Logic
    ai_action, ai_score = ai_brain.decide_action(news)
    market_trend, price = quant_brain.get_market_trend()
    
    print(f"\n--- AGENT STATUS REPORT ---")
    print(f"AI Sentiment: {ai_action} ({ai_score:.2f})")
    print(f"Market Trend: {market_trend} (${price:,.2f})")
    print("-" * 25)

    # 3. Execution & Result Capturing
    final_action = "HOLD/STANDBY"
    tx_hash = "N/A"

    if ai_action == "SPEND" and market_trend == "BEARISH":
        print("ACTION: AI and Math agree. INITIATING AUTONOMOUS TRANSFER...")
        final_action = "SPEND"
        burn_address = "0x000000000000000000000000000000000000dEaD"
        tx_hash = agent.send_transaction(burn_address, 0.001)
        print(f"🚀 SUCCESS! View on Etherscan: https://sepolia.etherscan.io/tx/{tx_hash}")
    else:
        print("ACTION: Signals mixed or positive. STANDING BY.")

    # 4. THE VITAL STEP: Logging the data
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "headline": news,
        "sentiment": round(ai_score, 4),
        "price": round(price, 2),
        "action": final_action,
        "tx_hash": tx_hash
    }
    
    log_decision(log_entry)
    print("📂 Decision recorded in logs/agent_history.csv")

if __name__ == "__main__":
    main()