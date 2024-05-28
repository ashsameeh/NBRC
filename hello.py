pip install -r requirements.txt
import streamlit as st  
from tenderr import make_output
import time


# Set page configuration including title and icon
st.set_page_config(page_title="ChatBot",
                   page_icon="🤔")
# Display the title of the chat interface
st.title("💭 Supply Chain Chatbot")
# Initialize session state to store chat messages if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []
# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# Accept user input in the chat interface
if prompt := st.chat_input("What is your question?"):
    # Display user input as a chat message
    with st.chat_message("user"):
        st.markdown(prompt)
    # Append user input to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # with st.spinner("Thinking..."):
    #     # Get response from the chatbot based on user input
    #     response = make_output(prompt)
    # Display a custom spinner while the chatbot thinks of an answer
    # Display a custom spinner while the chatbot thinks of an answer
    spinner_placeholder = st.empty()
    spinner_message = "Thinking"
    spinner_steps = 3

    def update_spinner(spinner_placeholder, spinner_message, spinner_steps):
        for i in range(spinner_steps):
            spinner_placeholder.text(f"{spinner_message}{'.' * (i % 4)}")
            time.sleep(0.5)

    update_spinner(spinner_placeholder, spinner_message, spinner_steps)

    # Get response from the chatbot based on user input
    response = make_output(prompt)

    spinner_placeholder.empty()
    
    
    # Display response from the chatbot as a chat message
    with st.chat_message("assistant"):
        # Write response with modified output (if any)
        st.write((response))
    # Append chatbot response to session state
    st.session_state.messages.append({"role": "assistant", "content": response})
    
