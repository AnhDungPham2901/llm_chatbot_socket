# Deploy LLM Chatbot with Socket Project

This project is an exploration of Python's socket capabilities, with a focus on streaming data between a server and a client, particularly handling the streaming output from a language model (LLM). The project implements a server that communicates with a client using sockets, and showcases the streaming of LLM responses in real-time.

## Project Overview

The goal of this project was to create a proof-of-concept application that demonstrates the power and complexity of streaming data using Python sockets. The server is capable of handling LLM streaming responses, requiring a customized `CallbackHandler` to meet the specific demands of streaming output. The client-side interface, created with Streamlit, provides a user-friendly and interactive experience for sending and receiving streamed data.

### Features

- **Socket-based Communication:** Establish and manage TCP connections between server and client.
- **LLM Streaming:** Stream the output of a language model in real-time, ensuring that the client receives the data as it's being generated.
- **Custom CallbackHandler:** Customize the `BaseCallbackHandler` to handle the streaming nature of LLM responses.
- **Streamlit UI:** A responsive and attractive user interface for the client side, providing an enhanced user experience.
- **Asynchronous Handling:** Implementation of synchronous communication with the intention to upgrade to asynchronous handling for improved performance. For more information on this, refer to the [Python documentation on `socketserver`](https://docs.python.org/3/library/socketserver.html).

### Demo Videos
[![Watch the demo](https://img.youtube.com/vi/QrYzI0e5vGg/maxresdefault.jpg)](https://www.youtube.com/watch?v=QrYzI0e5vGg)

### Completed Items

- Developed a server capable of handling socket connections and streaming data.
- Implemented a client that connects to the server via sockets and displays streaming data in real-time.
- Customized a `CallbackHandler` to manage the streaming of data from a language model (LLM).
- Created a Streamlit-based user interface for interactive communication with the server.
- Explored synchronous data handling with plans to upgrade to asynchronous communication for efficiency.

### How to Use

1. Install the requiremnts.txt and create file .env and put your OpenAI API Token
2. Edit the `config.py` file to fit with your use case
3. Start redis with port as your configuration file for chatbot memory
4. Start the server by running `server.py`
5. Open the Streamlit UI by running `streamlit run client_with_ui.py`.
6. Enter the input in the Streamlit text box and receive real-time responses from the LLM.

### Future Work

- **Asynchronous Upgrade:** Refactor the server and client code to support asynchronous communication, thus improving the scalability and responsiveness of the system.
- **Enhanced Streamlit UI:** Further improvements to the Streamlit interface for a more engaging user experience.
- **Robust Error Handling:** Implement comprehensive error handling mechanisms for network and LLM-related errors.

---

Thank you for exploring the Python Socket Experimentation Project. Your feedback and contributions are highly appreciated!
