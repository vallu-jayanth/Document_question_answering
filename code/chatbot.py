import streamlit as st
from streamlit_chat import message
import openai
import os
from indexing import query_engine

st.subheader("Clinical trial question answering")

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
    if question:
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

          