import streamlit as st
from streamlit_chat import message
import openai
import os
from indexing import query_engine

st.subheader("Clinical trial question answering")

with st.sidebar:
    openai_api_key = st.text_input('OpenAI API Key',key='chatbot_api_key',type="password")

os.environ["OPENAI_API_KEY"] = openai_api_key
openai.api_key=os.environ["OPENAI_API_KEY"]

if 'responses' not in st.session_state:
    st.session_state['responses'] = ["Hello!!, how can I assist you?"]

if 'requests' not in st.session_state:
    st.session_state['requests'] = []


# container for chat history
response_container = st.container()
# container for text box
textcontainer = st.container()


with textcontainer:
    question = st.text_input(
        "Ask questions from clinical trials cancer data",
        placeholder="Give me description of a study held recently?",
    )
    if question and not openai_api_key:
        st.info("please place your openai API key here to continue.....")
    if question and openai_api_key:
        with st.spinner("typing..."):            
            response = query_engine.query(question)
        st.session_state.requests.append(question)
        st.session_state.responses.append(response.response) 
with response_container:
    if st.session_state['responses']:

        for i in range(len(st.session_state['responses'])):
            message(st.session_state['responses'][i],key=str(i))
            if i < len(st.session_state['requests']):
                message(st.session_state["requests"][i], is_user=True,key=str(i)+ '_user')

          