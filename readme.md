# ChatBot Server & Frontend Application

This repository contains a ChatBot server developed using FastAPI which interacts with a PostgreSQL database to process user queries. There's also a frontend application designed using Streamlit that serves as an example UI for the ChatBot server.

## Prerequisites:

- Python 3.x
- PostgreSQL (installed and running on localhost:5432 by default)
- A `.env` file with required environment variables. You can generate one using `create_env_file.py`.

## Setting Up Backend:

### Step 1: Clone the Repository
```bash
git clone <repository_link>
cd <repository_directory>
```

### Step 2: Install Dependencies
```bash
pip install fastapi uvicorn psycopg2 python-dotenv openai streamlit
```

### Step 3: Create the .env File
Use the provided script to create a `.env` file with necessary configurations:

```bash
python create_env_file.py --api_key YOUR_OPENAI_API_KEY --db_pass YOUR_DB_PASSWORD --database YOUR_DB_NAME
```

**Note:** Replace placeholders like `YOUR_OPENAI_API_KEY` with actual values.

### Step 4: Start the Backend Server
```bash
python server.py
```
You should see a message: `OpenAPI key has been set, the server has been started!`

Your backend server is now running on `http://127.0.0.1:8001/`.

## Using Postman with Backend:

### 1. Get Root:
Send a GET request to `http://127.0.0.1:8001/` to get the server status.

### 2. Chat Query:
To chat with the bot, send a POST request to `http://127.0.0.1:8001/chatDB/query_database` with the following body:

```json
{
  "prompt": "YOUR_PROMPT_HERE",
  "chat_history": "YOUR_CHAT_HISTORY_HERE"
}
```

Replace `YOUR_PROMPT_HERE` and `YOUR_CHAT_HISTORY_HERE` with your desired values.

### 3. Get Conversation Name:
To get a name for a conversation based on a user query, send a POST request to `http://127.0.0.1:8001/conversation/get_name` with the body containing your query as a string.

## Running Frontend Application:

After setting up and running the backend server, you can run the Streamlit frontend as an example UI.

### Step 1: Start the Frontend Application:

```bash
cd frontend
streamlit run frontendApp.py
```

You'll see a new browser window/tab opening with the ChatBot UI. Here, you can input messages and interact with the ChatBot, view previous chats, and more.

## Conclusion:

This README provides steps to set up both the backend server and frontend application. Make sure the backend server is running when you're interacting with the frontend application. The server handles chat queries and also suggests conversation names based on user queries. The frontend serves as an example of how you can integrate and interact with the backend.

Developed by Sagar Dollin.