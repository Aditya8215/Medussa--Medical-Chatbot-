from flask import Flask, render_template, jsonify, request
from src.helper import download_embeddings
import weaviate, os
import weaviate.classes as wvc
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *

from langchain_weaviate import WeaviateVectorStore

import os

app=Flask(__name__)

load_dotenv()


gemini_api_key=os.environ.get("gemini_api_key=GOOGLE_API_KEY")
WEAVIATE_URL=os.environ.get("WEAVIATE_URL")
WEAVIATE_API_KEY=os.environ.get("WEAVIATE_API_KEY")
os.environ["WEAVIATE_URL"] = WEAVIATE_URL
os.environ["WEAVIATE_API_KEY"] = WEAVIATE_API_KEY
embeddings = download_embeddings()

# Connect to Weaviate Cloud
client= weaviate.connect_to_weaviate_cloud(
    cluster_url=WEAVIATE_URL,
    auth_credentials=wvc.init.Auth.api_key(WEAVIATE_API_KEY),
)
doc_search = WeaviateVectorStore(
    client=client,
    index_name="Medussa",
    embedding=embeddings,
    text_key="page_content"
)
retriever=doc_search.as_retriever(search_type='similarity',search_kwargs={"k":3})


chatModel = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    temperature=0.0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)
# Create the question-answer chain
question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
# Create the retrieval-augmented generation (RAG) chain
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input": msg})
    print("Response : ", response["answer"])
    return str(response["answer"])


@app.route("/")
def index():
    return render_template('chat.html')

if __name__=='__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)