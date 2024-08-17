from openai import OpenAI
import os
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain


def call_openai_api(messages, temperature = 0.9, max_tokens = 250):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=openai_api_key)
    
    return client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

def call_lang_chain(question, documents):
    llm = ChatOpenAI(model="gpt-3.5-turbo-0125")
    embeddings = OpenAIEmbeddings()

    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    vector_db = FAISS.from_documents(docs, embeddings)
    qa = ConversationalRetrievalChain.from_llm(
       llm=llm, 
       retriever= vector_db.as_retriever()
    )

    response = qa({"question":question, "chat_history": []})

    return response
    
# [
#     {
#     "role": "system",
#     "content": [
#         {
#         "type": "text",
#         "text": """
# You have to search for a product by it's name. Here is an input provided from user.\nPlease provide a list of product names in english on which you can filter the products. Return as mauch as you can please :). Result should be a JSON list of strings!!!! And do not add json word at the beginning.
# """
        
#         }
#     ]
#     },
#     {
#     "role": "user",
#     "content": [
#         {
#         "type": "text",
#         "text": search_phrase
#         }
#     ]
#     }
# ]
