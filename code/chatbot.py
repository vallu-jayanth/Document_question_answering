import streamlit as st
from streamlit_chat import message
import openai
import os
from llama_index import VectorStoreIndex, SimpleDirectoryReader


def save_uploadedfile(uploadedfile):
     with open(os.path.join("temp",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("file upoad success")


st.subheader("Insurance Q/A")

if 'responses' not in st.session_state:
    st.session_state['responses'] = ["Hello!!, how can I assist you?"]

if 'requests' not in st.session_state:
    st.session_state['requests'] = []

uploaded_file = st.file_uploader("Upload your insurance document", type="pdf")

# container for chat history
response_container = st.container()
# container for text box
textcontainer = st.container()


with textcontainer:
    question = st.text_input(
        "Ask questions from your insurance document",
        placeholder="what is the coverage of the insurance?",
        disabled=not uploaded_file,
    )
    if uploaded_file and question:
        with st.spinner("typing..."):
            save_uploadedfile(uploaded_file)
            documents = SimpleDirectoryReader("temp").load_data()
            index = VectorStoreIndex.from_documents(documents)
            os.remove(os.path.join("temp",uploaded_file.name))
            query_engine = index.as_query_engine()
            response = query_engine.query(question)
        st.session_state.requests.append(question)
        st.session_state.responses.append(response.response) 
with response_container:
    if st.session_state['responses']:

        for i in range(len(st.session_state['responses'])):
            message(st.session_state['responses'][i],key=str(i))
            if i < len(st.session_state['requests']):
                message(st.session_state["requests"][i], is_user=True,key=str(i)+ '_user')

          