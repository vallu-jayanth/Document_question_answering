import streamlit as st
import openai
import os
from llama_index import VectorStoreIndex, SimpleDirectoryReader


def save_uploadedfile(uploadedfile):
     with open(os.path.join("/Users/jay/Downloads/Insurance_QA/temp",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("file upoad success")


st.title("📝 File Q&A with Anthropic")
uploaded_file = st.file_uploader("Upload your insurance document", type="pdf")
question = st.text_input(
    "Ask questions from your insurance document",
    placeholder="what is the coverage of the insurance?",
    disabled=not uploaded_file,
)

# if uploaded_file and question and not openai_api_key:
#     st.info("Please add your openai API key to continue.")

# if uploaded_file and question and openai_api_key:
if uploaded_file and question:
    save_uploadedfile(uploaded_file)
    documents = SimpleDirectoryReader("/Users/jay/Downloads/Insurance_QA/temp").load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    response =  query_engine.query(question)
    print(response)
    st.write(response)