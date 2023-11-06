import socket
import streamlit as st

def show_page_config_title():
    st.set_page_config(
    page_title='Opus AI Assistance',
    page_icon='🤖'
    )
    st.title("Let's talk with Opus AI Assistant!!!")

def set_up_session_state():
    if 'messages' not in st.session_state:
        st.session_state.messages = []

def get_response_from_socket_server(data:str):
    HOST, PORT = "localhost", 9999
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))
        # Receive data from the server and shut down
        with st.chat_message("assistant"):
            message_placeholder = st.empty() # should be inside the block st.chat_message
            full_response = ""
            while True:
                chunk = sock.recv(1024)
                chunk = chunk.decode("utf-8")
                if chunk != "\n":
                    full_response += chunk
                message_placeholder.markdown(full_response)
                if not chunk:
                    break
        return full_response

show_page_config_title()
set_up_session_state()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    response = get_response_from_socket_server(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
