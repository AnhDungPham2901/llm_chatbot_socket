import sys
from typing import Any
import socketserver
from loguru import logger
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import MessagesPlaceholder
from langchain.memory import RedisChatMessageHistory
from langchain.prompts import HumanMessagePromptTemplate
from langchain.prompts import SystemMessagePromptTemplate
from langchain.memory import ConversationTokenBufferMemory
import config
from langchain.callbacks.base import BaseCallbackHandler

def get_user_context():
    """The purpose is to get the context to start a conversation
    The information will be get including:
        - Name
        - Some hightlight behaviours (get from context API)
    Returns:
        str: A prompt to tell the LLM to start the conversion with the extracted information
    """
    user_name = "UNKNOWN"
    actions_support = ['Search Job', 'Register Account', 'Disscuss FAQ']
    return user_name, actions_support

class CustomStreamingSocketCallbackHandler(BaseCallbackHandler):
    def __init__(self, wfile):
        super().__init__()
        self.wfile = wfile

    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        """Run on new LLM token. Only available when streaming is enabled."""
        try:
            self.wfile.write(token.encode('utf-8'))
            self.wfile.flush()

        except BrokenPipeError:
            # Handle a broken pipe error when the client disconnects
            logger.error("BrokenPipeError while writing to socket")
            pass
        except Exception as e:
            # Handle other exceptions that may occur
            print(f"Error writing to socket: {e}", file=sys.stderr)

class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        # Read the client's message
        self.data = self.rfile.readline().strip().decode('utf-8')
        logger.info(f"{self.client_address[0]} wrote: {self.data}")
        streaming_handler = CustomStreamingSocketCallbackHandler(self.wfile)
        # Now we need to feed this input to the LLM and stream the output back
        self.interact_init_conversation_agent(self.data, self.generate_session_id(), streaming_handler)


    def interact_init_conversation_agent(self, user_input: str, session_id: str, streaming_handler):
        logger.info("Interacting with INIT AGENT")
        system_message_path = "init_agent_prompt_template.txt"
        with open(system_message_path, 'r') as file:
            init_agent_prompt_template = file.read()
        llm = ChatOpenAI(temperature=0.5, model_name='gpt-4', streaming=True,
                        callbacks=[streaming_handler])
        prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(init_agent_prompt_template),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{human_input}")
            ],
        )
        agent_name = config.AGENT_CONFIG_DICT['agent_name']
        agent_role = config.AGENT_CONFIG_DICT['agent_role']
        company_name = config.AGENT_CONFIG_DICT['company_name']
        company_introduction = config.AGENT_CONFIG_DICT['company_introduction']
        company_values = config.AGENT_CONFIG_DICT['company_values']
        service_overview_config = config.SERVICE_OVERVIEW_CONFIG 
        user_name, available_servies = get_user_context()

        history = RedisChatMessageHistory(session_id=session_id, 
                                        url=config.CHATBOT_MEMORY_CONFIG['url'], 
                                        key_prefix=config.CHATBOT_MEMORY_CONFIG['key_prefix'])
        memory = ConversationTokenBufferMemory(
            memory_key="chat_history", chat_memory=history, return_messages=True, 
            max_token_limit=2000, llm=llm, input_key="human_input"
        )
        llm_router = LLMChain(llm=llm, prompt=prompt, verbose=False, memory=memory)

        response = llm_router.predict(
            agent_name=agent_name, agent_role=agent_role, available_servies=available_servies, 
            company_introduction=company_introduction, company_name=company_name, 
            company_values=company_values, user_name=user_name, 
            service_overview_config=service_overview_config,human_input=user_input
        )
        return response

    def generate_session_id(self):
        """Generate session_id for chatbot memory redis"""
        return "testing_socket"

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()

