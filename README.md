# 🤖 AI Chatbot Assistant

An interactive **AI Chatbot Assistant** built with **Python, Streamlit, OpenAI, and LangChain**. The application provides a user-friendly chat interface where users can ask questions and receive AI-generated responses.

The chatbot supports conversation history, coding assistance, explanations, creative writing, and general knowledge questions.

---

## ✨ Features

* 🤖 AI-powered conversational chatbot
* 💬 Interactive chat interface
* 🧠 Conversation history and context
* 🔑 Secure API key input through the sidebar
* 🔒 API key is stored only during the current session
* 📊 Chat statistics
* 🗑️ Clear chat history option
* ⚙️ Sidebar configuration
* 🎨 Custom CSS styling
* ⏳ Loading/spinner while generating responses
* ⚠️ Error handling for API and application errors
* 💻 Coding assistance
* 📚 Detailed explanations
* ✍️ Creative writing support
* 🌐 General knowledge assistance

---

## 🛠️ Technologies Used

### 1. Python

Python is the main programming language used to develop the chatbot application.

### 2. Streamlit

Streamlit is used to create the web-based user interface, including the sidebar, chat input, buttons, metrics, and messages. The application configures its page using Streamlit's page configuration functionality.

### 3. OpenAI

OpenAI provides the Large Language Model used to generate chatbot responses. The application uses the **GPT-3.5-Turbo** model through `ChatOpenAI`.

### 4. LangChain

LangChain is used to connect the prompt template, language model, conversation history, and output parser into an AI processing chain.

Main LangChain components used include:

* `ChatPromptTemplate`
* `MessagesPlaceholder`
* `HumanMessage`
* `AIMessage`
* `StrOutputParser`
* `ChatOpenAI`

### 5. HTML & CSS

Custom HTML and CSS are used to improve the appearance of the chatbot, including message boxes, buttons, headers, colors, spacing, and layout.

### 6. Session State

Streamlit's `session_state` is used to maintain:

* Chat messages
* API key
* Chat initialization status

This allows the application to preserve conversation information while the user interacts with the app.

---

## 📂 Project Structure

```text
AI-Chatbot-Assistant/
│
├── main.py
├── requirements.txt
└── README.md
```

### `main.py`

The main application file containing the Streamlit interface, LangChain configuration, OpenAI integration, chat history, and response generation.

### `requirements.txt`

Contains the Python packages required to run the project.

### `README.md`

Provides project documentation, setup instructions, technologies, and usage information.

---

## 📦 Requirements

The project uses packages including:

```text
streamlit
langchain
langchain-core
langchain-openai
openai
python-dotenv
pydantic
SQLAlchemy
wikipedia
pinecone
langchain-pinecone
```

Your current requirements file also contains additional LangChain and Pinecone-related packages.

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Then move into the project directory:

```bash
cd YOUR-REPOSITORY
```

---

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 OpenAI API Key

The application requires an **OpenAI API key**.

When the application starts:

1. Open the sidebar.
2. Enter your OpenAI API key.
3. Click **Initialize Chat**.
4. Start asking questions.

The application checks that the entered key begins with `sk-` before initializing the chat.

> ⚠️ **Important:** Never upload your API key to GitHub or put it directly inside your source code.

---

## ▶️ Run the Application

Run the following command from the project folder:

```bash
streamlit run main.py
```

Streamlit will start the application and provide a local web address where you can access the chatbot.

---

## 💬 How to Use

1. Launch the application.
2. Enter your OpenAI API key in the sidebar.
3. Click **Initialize Chat**.
4. Type your question in the chat input.
5. The AI assistant generates a response.
6. Previous messages are maintained as conversation history.
7. Use **Clear Chat History** to start a new conversation.

The application builds a LangChain prompt containing a system instruction, previous conversation history, and the user's current input.

---

## 📊 Chat Statistics

The sidebar displays:

* **Total Messages**
* **User Messages**
* **Assistant Messages**

These values are calculated from the current Streamlit session's message history.

---

## 🧠 AI Processing Flow

```text
User
  │
  ▼
Streamlit Chat Interface
  │
  ▼
User Input
  │
  ▼
Chat History
  │
  ▼
LangChain Prompt Template
  │
  ▼
OpenAI GPT-3.5-Turbo
  │
  ▼
StrOutputParser
  │
  ▼
AI Response
  │
  ▼
Streamlit Chat Interface
```

The core chain is:

```text
Prompt Template → OpenAI LLM → Output Parser
```

This is implemented using LangChain's runnable pipeline.

---

## 🎯 Use Cases

This chatbot can be used for:

* 📚 Educational questions
* 💻 Programming assistance
* 🧠 Concept explanations
* ✍️ Creative writing
* 🌐 General knowledge
* 📝 Study assistance
* 🔍 Question answering

---

## 🔐 Security

The application accepts the OpenAI API key through a password-type input field and keeps it in Streamlit's session state rather than saving it permanently.

For production deployment, environment variables or a secure secrets-management mechanism should be preferred.

---

## ⚠️ Error Handling

If an error occurs while communicating with the AI model, the application catches the exception and displays an error message to the user instead of terminating the interface.

---

## 🔮 Future Improvements

Possible improvements include:

* 🔐 Use Streamlit Secrets for API key management
* 💾 Persistent conversation storage
* 📄 PDF/document question answering
* 🗃️ Vector database integration
* 🔎 RAG-based question answering
* 🎤 Voice input
* 🔊 Text-to-speech responses
* 🌙 Dark/light theme options
* 👥 User authentication
* 📈 Advanced analytics
* 🤖 Support for newer OpenAI models

---

## 👩‍💻 Author

**Aqsa Ahmad**

AI Chatbot Assistant Project

---

## 📄 License

This project is developed for educational and learning purposes.
