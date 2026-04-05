# 🤖 Sovereign AI Quant Agent (SAQA)

**A Self-Sovereign Financial Entity integrating Machine Learning, Quantitative Analysis, and Blockchain Infrastructure.**

---

## 📌 Project Overview
The **Sovereign AI Quant Agent** is an autonomous "Hedge Fund of One." By merging **NLP Sentiment Analysis**, **Quantitative Mathematical Models**, and **Ethereum Smart Contracts**, this agent operates as an independent economic actor. It doesn't just predict the market—it has the power to settle its own transactions.

### 🎯 The "Triple-Threat" Pillar Logic
To build a truly autonomous system in 2026, one must master three distinct domains:

1.  **Machine Learning (The Brain):** Used to process "Unstructured Data" (News/Social Media). It turns human emotion and global events into a machine-readable sentiment score.
2.  **Quant Finance (The Logic):** Acts as the "Statistical Filter." It uses hard math (Moving Averages/Volatility) to ensure the AI doesn't act on "hype" without market confirmation.
3.  **Blockchain (The Infrastructure):** Provides "Infrastructural Sovereignty." It gives the AI a digital identity (ECDSA Wallet) and a way to move value without a middleman or a bank account.

---

## 🏗️ Technical Architecture



### 1. Data Ingestion & NLP (The Senses)
The agent utilizes `TextBlob` for Natural Language Processing.
* **Mechanism:** Polarity scoring of news headlines.
* **Range:** `-1.0` (Bearish/Panic) to `+1.0` (Bullish/Euphoria).

### 2. Quantitative Strategy (The Filter)
The agent pulls live time-series data via `yfinance`.
* **Indicator:** 3-Day Simple Moving Average (SMA).
* **Rule:** If `Price < SMA`, the Quant engine flags a "Bearish Regime," overriding any positive AI sentiment to protect capital.



### 3. On-Chain Execution (The Hand)
Using `Web3.py`, the agent manages its own Private Keys securely.
* **Sovereignty:** Transactions are signed locally and broadcasted to the Sepolia Testnet.
* **Transparency:** Every decision is immutable and auditable on the blockchain.

---

## 📅 Project Timeline & Roadmap

### **Phase 1: Identity & Security (Completed)**
* [x] Established professional Monorepo structure.
* [x] Developed `identity.py` for autonomous wallet generation.
* [x] Funded Agent with **0.05 Sepolia ETH** for operational gas fees.
* [x] Implemented `.env` and `.gitignore` for industrial-grade secret management.

### **Phase 2: Multimodal Intelligence (Completed)**
* [x] Integrated `brain.py` (NLP Sentiment).
* [x] Developed `quant_brain.py` (Market Trend Math).
* [x] Created `run_agent.py` Signal Merger (Hybrid Decision Logic).

### **Phase 3: Autonomous Settlement (Current)**
* [ ] **Next Step:** Implement `send_transaction()` to enable the Agent to move funds.
* [ ] Build an automated 60-minute "Check-and-Act" Cron Loop.
* [ ] Research: Integrate **zkML (Zero-Knowledge ML)** to prove AI decision integrity on-chain.

---

## 🛠️ Installation & Setup

1. **Clone the Repo:**
   ```powershell
   git clone [https://github.com/Ghostofficial141/sovereign-ai-agent.git](https://github.com/Ghostofficial141/sovereign-ai-agent.git)
   cd sovereign-ai-agent