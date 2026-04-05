from textblob import TextBlob

class AIAgentBrain:
    def decide_action(self, text):
        # 1. Analyze the 'vibe' of the text
        analysis = TextBlob(text)
        sentiment = analysis.sentiment.polarity  # Score from -1.0 to 1.0
        
        # 2. Decide based on score
        if sentiment > 0.1:
            return "SAVE", sentiment
        elif sentiment < -0.1:
            return "SPEND", sentiment
        else:
            return "HOLD", sentiment

if __name__ == "__main__":
    brain = AIAgentBrain()
    print(brain.decide_action("The market is crashing!")) # Should say SPEND