
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
import os

# Page Configuration
st.set_page_config(
    page_title="AI Chatbot Assistant",
    page_icon="🤖",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        background: linear-gradient(45deg, #1E88E5, #00BCD4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 1rem 0;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        max-width: 80%;
        color : #101010;
    }
    .user-message {
        background-color: #E3F2FD;
        margin-left: auto;
        border: 1px solid #1E88E5;
        color: #101010;
    }
    .assistant-message {
        background-color: #F5F5F5;
        margin-right: auto;
        border: 1px solid #BDBDBD;
    }
    .stButton>button {
        background: linear-gradient(45deg, #1E88E5, #00BCD4);
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 15px rgba(30, 136, 229, 0.4);
    }
    .api-warning {
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #FF9800;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "api_key" not in st.session_state:
    st.session_state.api_key = ""
if "chat_initialized" not in st.session_state:
    st.session_state.chat_initialized = False

# Title
st.markdown('<p class="main-header">🤖 AI Chatbot Assistant</p>', unsafe_allow_html=True)

# Sidebar - API Key Configuration
with st.sidebar:
    st.title("⚙️ Configuration")
    
    st.markdown("### 🔑 API Key Required")
    st.markdown("Please enter your OpenAI API key to start chatting.")
    
    api_key_input = st.text_input(
        "OpenAI API Key",
        type="password",
        placeholder="sk-...",
        value=st.session_state.api_key if st.session_state.api_key else ""
    )
    
    if st.button("✅ Initialize Chat", use_container_width=True):
        if api_key_input and api_key_input.startswith("sk-"):
            st.session_state.api_key = api_key_input
            st.session_state.chat_initialized = True
            st.session_state.messages = []  # Clear previous messages
            st.rerun()
        else:
            st.error("⚠️ Please enter a valid OpenAI API key starting with 'sk-'")
    
    if st.session_state.chat_initialized:
        st.success("✅ Chat initialized successfully!")
        
        if st.button("🔄 Clear Chat History", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
    
    st.divider()
    st.markdown("### 📊 Chat Statistics")
    st.metric("Total Messages", len(st.session_state.messages))
    st.metric("User Messages", len([m for m in st.session_state.messages if m["role"] == "user"]))
    st.metric("Assistant Messages", len([m for m in st.session_state.messages if m["role"] == "assistant"]))
    
    st.divider()
    st.markdown("### 💡 Tips")
    st.info("""
    - Ask any question
    - Get detailed explanations
    - Code assistance available
    - Creative writing support
    """)
    
    # Show example if no API key
    
if not st.session_state.chat_initialized:
    st.markdown("""
    <div class="api-warning">
        <h3>🔑 Welcome to AI Chatbot!</h3>
        <p>To get started, please:</p>
        <ol>
            <li>Enter your OpenAI API key in the sidebar</li>
            <li>Click "Initialize Chat" button</li>
            <li>Start chatting!</li>
        </ol>
        <p style="font-size: 0.9rem; color: #101010; margin-top: 0.5rem;">
            🔒 Your API key is stored only in your session and never saved.
        </p>
    </div>
    """, unsafe_allow_html=True)

else:
    # Display chat messages
    chat_container = st.container()
    
    with chat_container:
        for message in st.session_state.messages:
            role = message["role"]
            content = message["content"]
            
            if role == "user":
                st.markdown(f"""
                <div class="chat-message user-message">
                    <strong> You:</strong><br>{content}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="chat-message assistant-message">
                    <strong>🤖 Assistant:</strong><br>{content}
                </div>
                """, unsafe_allow_html=True)
    
    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with chat_container:
            st.markdown(f"""
            <div class="chat-message user-message">
                <strong> You:</strong><br>{prompt}
            </div>
            """, unsafe_allow_html=True)
        
        # Generate response
        with st.spinner(" Thinking..."):
            try:
                # Initialize LangChain
                llm = ChatOpenAI(
                    model="gpt-3.5-turbo",
                    temperature=0.7,
                    api_key=st.session_state.api_key
                )
                
                # Create prompt template with history
                prompt_template = ChatPromptTemplate.from_messages([
                    ("system", """You are a helpful AI assistant. You provide clear, 
                    detailed, and accurate responses. You can help with coding, 
                    explanations, creative writing, and general knowledge questions."""),
                    MessagesPlaceholder(variable_name="chat_history"),
                    ("human", "{input}")
                ])
                
                # Create chain
                chain = prompt_template | llm | StrOutputParser()
                
                # Prepare chat history
                chat_history = []
                for msg in st.session_state.messages[:-1]:  # Exclude current message
                    if msg["role"] == "user":
                        chat_history.append(HumanMessage(content=msg["content"]))
                    else:
                        chat_history.append(AIMessage(content=msg["content"]))
                
                # Get response
                response = chain.invoke({
                    "input": prompt,
                    "chat_history": chat_history
                })
                
                # Add assistant response to history
                st.session_state.messages.append({"role": "assistant", "content": response})
                
                # Display assistant response
                with chat_container:
                    st.markdown(f"""
                    <div class="chat-message assistant-message">
                        <strong>🤖 Assistant:</strong><br>{response}
                    </div>
                    """, unsafe_allow_html=True)
                
            except Exception as e:
                error_msg = f"⚠️ Error: {str(e)}"
                st.error(error_msg)
                
                # Display error in chat
                with chat_container:
                    st.markdown(f"""
                    <div class="chat-message assistant-message" style="border-color: #F44336;">
                        <strong>🤖 Assistant:</strong><br>{error_msg}
                    </div>
                    """, unsafe_allow_html=True)

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9rem;">
    🤖 AI Chatbot Assistant | Powered by OpenAI & LangChain
</div>
""", unsafe_allow_html=True)