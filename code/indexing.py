import requests
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index import StorageContext, load_index_from_storage

documents = SimpleDirectoryReader('sampling').load_data()
print("****starting to index******")
index = VectorStoreIndex.from_documents(documents)
print("******created index********")
index.storage_context.persist()
# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="./storage")
# load index
print("*************loading index**********")
index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine()
print(query_engine.query("Give me three descriptions of the study from different records?"))