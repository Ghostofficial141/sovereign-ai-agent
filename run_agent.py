from agent.identity import AIAgent
from agent.brain import AIAgentBrain
from agent.quant_brain import QuantBrain
from agent.notifier import DiscordNotifier
import csv
import os
import time
from datetime import datetime

def log_decision(data):
    file_path = "logs/agent_history.csv"
    if not os.path.exists("logs"): os.makedirs("logs")
    file_exists = os.path.isfile(file_path)
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        fieldnames = ["timestamp", "headline", "sentiment", "price", "action", "tx_hash"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists: writer.writeheader()
        writer.writerow(data)

def main():
    try:
        # Initialize System Components
        agent = AIAgent()
        ai_brain = AIAgentBrain()
        quant_brain = QuantBrain()
        notifier = DiscordNotifier()
        
        # 1. Sensing (The Input)
        news = "Global economic crisis causes markets to plummet."
        
        # 2. Thinking (The Analysis)
        ai_action, ai_score = ai_brain.decide_action(news)
        market_trend, price = quant_brain.get_market_trend()
        
        print(f"\n--- AGENT STATUS REPORT [{datetime.now().strftime('%H:%M:%S')}] ---")
        print(f"AI Sentiment: {ai_action} ({ai_score:.2f})")
        print(f"Market Trend: {market_trend} (${price:,.2f})")

        # 3. Acting (The Execution)
        final_action = "HOLD/STANDBY"
        tx_hash = "N/A"

        if ai_action == "SPEND" and market_trend == "BEARISH":
            print("🚨 CONSENSUS REACHED: Initiating Transaction...")
            final_action = "SPEND"
            target_address = "0x000000000000000000000000000000000000dEaD" # Burn address
            tx_hash = agent.send_transaction(target_address, 0.001)
            
            notifier.send_message(f"🚀 **CRITICAL:** Sent 0.001 ETH.\nTX: `{tx_hash}`")
        else:
            print("✅ STATUS: Signals mixed/stable. Standing by.")
            notifier.send_message(f"📊 **REPORT:** Market stable at ${price:,.2f}. No action required.")

        # 4. Remembering (The Persistence)
        log_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "headline": news,
            "sentiment": round(ai_score, 4),
            "price": round(price, 2),
            "action": final_action,
            "tx_hash": tx_hash
        }
        log_decision(log_entry)

    except Exception as e:
        print(f"❌ SYSTEM ERROR: {e}")

if __name__ == "__main__":
    print("🚀 SOVEREIGN AGENT ONLINE. Monitoring every 60 minutes...")
    while True:
        try:
            main()
            print("💤 Cycle complete. Sleeping for 1 hour...")
            time.sleep(3600) 
        except KeyboardInterrupt:
            print("\n🛑 Shutdown command received. Goodbye.")
            break