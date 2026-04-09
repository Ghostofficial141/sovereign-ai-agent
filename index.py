import streamlit as st
import pandas as pd
from agent.brain import AIAgentBrain
from agent.quant_brain import QuantBrain
from agent.notifier import DiscordNotifier

st.set_page_config(page_title="Sovereign AI Dashboard", page_icon="🤖")

st.title("🤖 Sovereign AI Agent Dashboard")
st.markdown("---")

# Sidebar for controls
st.sidebar.header("Agent Controls")
run_agent = st.sidebar.button("Execute Manual Audit")

# Initialize brains
brain = AIAgentBrain()
quant = QuantBrain()

# Display Market Data
st.subheader("📊 Real-time Market Analysis")
trend, price = quant.get_market_trend()
col1, col2 = st.columns(2)
col1.metric("BTC Price", f"${price:,.2f}")
col2.metric("Market Trend", trend)

# Logic for Manual Trigger
if run_agent:
    with st.spinner("Agent is analyzing news and technicals..."):
        news = "Global economic shift impacts crypto liquidity."
        action, score = brain.decide_action(news)
        
        st.success(f"Decision: **{action}** (Sentiment Score: {score})")
        
        # Send to Discord
        notifier = DiscordNotifier()
        notifier.send_message(f"🖥️ **STREAMLIT TRIGGER:** Agent analyzed market at ${price}. Action: {action}")
        st.balloons()

# Show Logs
st.subheader("📜 Recent Activity Logs")
try:
    df = pd.read_csv("logs/agent_history.csv")
    st.dataframe(df.tail(10), use_container_width=True)
except:
    st.info("No local logs found. Run the agent to generate data.")