from agent.identity import AIAgent
from agent.brain import AIAgentBrain
from agent.quant_brain import QuantBrain

def main():
    # Load our Agent, AI, and Quant Math
    agent = AIAgent()
    ai_brain = AIAgentBrain()
    quant_brain = QuantBrain()
    
    # 1. Provide a News Headline
    news = "Global economic crisis causes markets to plummet."
    
    # 2. Get the "Feel" and the "Math"
    ai_action, ai_score = ai_brain.decide_action(news)
    market_trend, price = quant_brain.get_market_trend()
    
    print(f"--- DAY 2 REPORT ---")
    print(f"AI Sentiment: {ai_action} ({ai_score})")
    print(f"Market Trend: {market_trend} (${price:.2f})")

    # 3. The Logic: Only act if both agree
    if ai_action == "SPEND" and market_trend == "BEARISH":
        print("ACTION: AI and Math agree. PREPARING TRANSACTION...")
    else:
        print("ACTION: Signals mixed. STANDING BY.")

if __name__ == "__main__":
    main()