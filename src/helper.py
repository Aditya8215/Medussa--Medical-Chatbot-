from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
from langchain.schema import Document 
# Extract PDF Files
def load_pdfs(directory):
    loader=DirectoryLoader(
        directory,
        glob='*.pdf',
        loader_cls=PyPDFLoader
    )
    documents=loader.load()
    return documents

 # Document is a object that is used for compatability 

def filter_extracted_data(docs:List[Document])->List[Document]:
    """
    Filter out extracted data """
    filter_data:List[Document]=[]
    for doc in docs:
        src=doc.metadata.get('source')
        filter_data.append(
            Document(
                page_content=doc.page_content,
                metadata={'source':src}
            )
        )
    return filter_data

# Split the documents into smaller chunks
def text_split(minimal_docs):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=10,    # For understanding the context
    )
    texts_chunks=text_splitter.split_documents(minimal_docs)
    return texts_chunks

from langchain.embeddings import HuggingFaceEmbeddings
def download_embeddings():
    model_name="NeuML/pubmedbert-base-embeddings"
    embeddings=HuggingFaceEmbeddings(
        model_name=model_name
    )
    return embeddings