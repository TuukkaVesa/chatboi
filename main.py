from mqtt.mqtt_client import connect_broker
from openai_api.openai_client import query_openai
from cache.cache_manager import ConversationCache

# Initialize the conversation cache
conversation_cache = ConversationCache()

# Function to handle user input
def handle_user_input(user_input):
    # Get the conversation context
    context = conversation_cache.get_conversation()
    # Query OpenAI for a response
    response = query_openai(user_input, context)
    # Add the user input and response to the cache
    conversation_cache.add_message(user_input, response)
    return response

if __name__ == "__main__":
    # Connect to the MQTT broker
    connect_broker("localhost", 1883)

    # Example usage
    user_input = "What is the status of machine X?"
    bot_response = handle_user_input(user_input)
    print(f"Bot: {bot_response}")
