import re

class RuleBasedChatbot:
    def __init__(self):
        self.history = []
        self.intents = {
            r"(hi|hello|hey)": "Hello! How can I help you today?",
            r"(bye|goodbye|see you)": "Goodbye! Have a nice day!",
            r"(help|support)": "You can ask me about our services, timings, or general queries.",
            r"(how are you|how's it going)": "I'm just a bot, but I'm here to help!",
            r"(thank you|thanks)":"Its my pleasure, anything want"
        }
        self.knowledge_base = {
            "what are your hours": "We are open from 9 AM to 5 PM, Monday to Friday.",
            "location": "We are located in Bangalore, India.",
            "services": "We offer IT consulting, software development, and AI solutions."
        }

    def get_response(self, user_input):
        # 1. Check intents (pattern matching)
        for pattern, response in self.intents.items():
            if re.search(pattern, user_input.lower()):
                self.log(user_input, response)
                return response
        
        # 2. Check knowledge base (exact match)
        for question, answer in self.knowledge_base.items():
            if question in user_input.lower():
                self.log(user_input, answer)
                return answer
        
        # 3. Fallback response
        fallback = "Sorry, I didn't understand that. Can you rephrase your question?"
        self.log(user_input, fallback)
        return fallback

    def log(self, user_input, response):
        self.history.append({"user": user_input, "bot": response})

    def show_history(self):
        print("\nConversation History:")
        for chat in self.history:
            print(f"You: {chat['user']}\nBot: {chat['bot']}")

def main():
    bot = RuleBasedChatbot()
    print("Welcome to SyntexHub Chatbot! (type 'exit' to finish)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            bot.show_history()
            print("Chat ended.")
            break
        response = bot.get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
