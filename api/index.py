from http.server import BaseHTTPRequestHandler
from agent.identity import AIAgent
from agent.brain import AIAgentBrain
from agent.quant_brain import QuantBrain
from agent.notifier import DiscordNotifier

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Initialize
            agent = AIAgent()
            ai_brain = AIAgentBrain()
            quant_brain = QuantBrain()
            notifier = DiscordNotifier()

            # Logic
            news = "Global economic crisis causes markets to plummet."
            ai_action, ai_score = ai_brain.decide_action(news)
            market_trend, price = quant_brain.get_market_trend()

            if ai_action == "SPEND" and market_trend == "BEARISH":
                burn_address = "0x000000000000000000000000000000000000dEaD"
                tx_hash = agent.send_transaction(burn_address, 0.001)
                notifier.send_message(f"🚀 **VERCEL CRON:** Sent 0.001 ETH. TX: `{tx_hash}`")
            else:
                notifier.send_message(f"📊 **VERCEL REPORT:** Market at ${price:,.2f}. Standing by.")

            self.send_response(200)
            self.end_headers()
            self.w3.write("Agent Cycle Complete".encode())
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.w3.write(f"Error: {e}".encode())