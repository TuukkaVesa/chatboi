Here's a sample **README.md** for your **UNS Chat Bot** project. This file includes a project description, setup instructions, and explanations of the various components in your codebase.

---

# UNS Chat Bot

This project is a Unified Namespace (UNS) Chat Bot that interacts with an MQTT broker (via EMQX), OpenAI API for natural language processing, and a Predictive Maintenance API to provide intelligent responses and predictive analytics for an industrial environment.

The bot is designed to:
- Subscribe to relevant MQTT topics from the Unified Namespace (UNS).
- Interpret user queries in natural language (via OpenAI API).
- Provide machine status, control commands, and maintenance predictions.

## Table of Contents
1. [Project Setup](#project-setup)
2. [Project Structure](#project-structure)
3. [Usage](#usage)
4. [APIs Used](#apis-used)
5. [Caching Strategy](#caching-strategy)
6. [Contributing](#contributing)
7. [License](#license)

---

## Project Setup

### Prerequisites

To run the project, you need to have the following installed on your machine:

- **Python 3.8+**
- **PyCharm IDE** (recommended, but optional)
- **pip** (Python package manager)

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/UNS_Chat_Bot.git
    cd UNS_Chat_Bot
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # For Linux/MacOS
    .venv\Scripts\activate     # For Windows
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your API keys:
    - **OpenAI API**: Add your OpenAI API key to the `openai_client.py` file under the `openai.api_key` variable.
    - **Predictive Maintenance API**: If using a predictive maintenance API, update the API URL and credentials in `predictive_client.py`.

## Project Structure

```bash
UNS_Chat_Bot/
│
├── cache/                      # Manages conversation history and context
│   ├── __init__.py
│   ├── cache_manager.py         # Handles sliding window and session management
│
├── mqtt/                       # MQTT-related functionality
│   ├── __init__.py
│   ├── mqtt_client.py           # Handles connection and interaction with EMQX broker
│
├── openai_api/                 # Handles interactions with OpenAI API
│   ├── __init__.py
│   ├── openai_client.py         # Sends queries to OpenAI and retrieves responses
│
├── predictive_api/             # Integrates with Predictive Maintenance API
│   ├── __init__.py
│   ├── predictive_client.py     # Sends data to predictive analytics API
│
├── utils/                      # Utility functions (e.g., logging)
│   ├── __init__.py
│   ├── logger.py                # Logs activity and errors
│
├── main.py                     # Main entry point to run the chat bot
├── requirements.txt            # Python dependencies
└── README.md                   # Project description and instructions
```

### Key Files

- **`main.py`**: This is the entry point of the project. It ties together the MQTT broker connection, the OpenAI API, and the Predictive Maintenance API. This file handles user input, retrieves context, and provides intelligent responses.
- **`mqtt/mqtt_client.py`**: Manages the connection to the MQTT broker (EMQX), subscribes to topics, and processes incoming messages.
- **`openai_api/openai_client.py`**: Handles communication with OpenAI to process natural language queries and generate responses.
- **`predictive_api/predictive_client.py`**: Sends data to the predictive maintenance API and retrieves predictions for machine health and maintenance.
- **`cache/cache_manager.py`**: Manages conversation history and context using a sliding window or summarization technique to avoid excessive memory usage.
- **`utils/logger.py`**: Provides a logging utility for the bot to track activity and errors.

## Usage

1. **Run the Chat Bot**:
   Once everything is set up, you can start the chat bot using the following command:
   ```bash
   python main.py
   ```

2. **User Interaction**:
   The bot will interact with users by interpreting natural language queries (like "What is the status of machine X?") and providing machine statuses, control commands, and maintenance predictions using the APIs integrated.

3. **Example Interaction**:
   ```bash
   User: What is the status of machine X?
   Bot: Machine X is currently operational and running at 85% efficiency.
   ```

## APIs Used

1. **OpenAI API**:
   - Used for processing user queries and generating intelligent responses.
   - You need an API key from OpenAI (https://beta.openai.com/signup/).
   
2. **Predictive Maintenance API**:
   - Provides predictive insights into machine health, failure predictions, and maintenance schedules.
   - Update the API URL and credentials in the `predictive_client.py` file as per the API service you are using (e.g., Google Cloud AI, Azure ML).

## Caching Strategy

To prevent memory overload and high costs from sending too much data to the OpenAI API, the bot employs a **sliding window cache** to store recent conversations. This cache maintains the last 5 interactions by default, ensuring context is preserved without excessive memory use.

Additionally, older context can be summarized to keep important information while discarding unnecessary details.

- **ConversationCache Class**:
  - Adds user and bot messages to the cache.
  - Retrieves the current conversation context for the OpenAI API.
  - Automatically resets the cache after a period of inactivity.

## Contributing

Contributions are welcome! Please follow the guidelines below:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
'd like to add anything specific or need further customization for the README!