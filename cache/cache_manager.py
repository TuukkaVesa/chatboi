class ConversationCache:
    def __init__(self, max_size=5):
        self.cache = []
        self.max_size = max_size

    def add_message(self, user_input, bot_response):
        if len(self.cache) >= self.max_size:
            self.cache.pop(0)  # Remove oldest message pair
        self.cache.append((user_input, bot_response))

    def get_conversation(self):
        return "\n".join([f"User: {u}\nBot: {b}" for u, b in self.cache])

# Extend this class with summarization and timeouts as needed
